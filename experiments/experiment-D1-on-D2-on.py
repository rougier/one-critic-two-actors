# -----------------------------------------------------------------------------
# Copyright (c) 2016, Nicolas P. Rougier
# Distributed under the (new) BSD License.
# -----------------------------------------------------------------------------
import numpy as np
from data.stats import stats
from experiment import Experiment
from data.theoretical.data import get


def session(exp):
    exp.model.setup()
    records = np.zeros((exp.n_block, exp.n_trial),
                       dtype=exp.task.records.dtype)

    # Day 1 : GPi ON
    for trial in exp.task:
        exp.model.process(exp.task, trial, model=exp.model)
    records[0] = exp.task.records

    # Day 2: GPi ON
    for trial in exp.task:
        exp.model.process(exp.task, trial, model=exp.model)
    records[1] = exp.task.records

    return records


experiment = Experiment(model="model.json", task="task.json",
                        result="data/theoretical/D1-on-D2-on.npy",
                        report="data/theoretical/D1-on-D2-on.txt",
                        n_session=12, n_block=2, seed=437)
records = experiment.run(session, "D1-on-D2-on")

n = 10
# Get all data on day 0 where gpi is active
D1 = get('11', day=0, gpi=1, n_trial=60, key='success')
# Get all data on day 1 where gpi is inactive
D2 = get('11', day=1, gpi=1, n_trial=60, key='success')

D1_start = [np.mean(session[:n]) for session in D1]
D1_end = [np.mean(session[-n:]) for session in D1]
D2_start = [np.mean(session[:n]) for session in D2]
D2_end = [np.mean(session[-n:]) for session in D2]

print("D1 start: %.3f  ±%.3f (std)  ±%.3f (sem)" % stats(D1_start))
print("D1 end:   %.3f  ±%.3f (std)  ±%.3f (sem)" % stats(D1_end))
print("D2 start: %.3f  ±%.3f (std)  ±%.3f (sem)" % stats(D2_start))
print("D2 end:   %.3f  ±%.3f (std)  ±%.3f (sem)" % stats(D2_end))
print()
