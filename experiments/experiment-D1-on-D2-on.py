# -----------------------------------------------------------------------------
# Copyright (c) 2016, Nicolas P. Rougier
# Distributed under the (new) BSD License.
# -----------------------------------------------------------------------------
import numpy as np
from experiment import Experiment


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
                        n_session=12, n_block=2, seed=422)
records = experiment.run(session, "D1-on-D2-on")

