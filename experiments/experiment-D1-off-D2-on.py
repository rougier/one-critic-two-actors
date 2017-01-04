# -----------------------------------------------------------------------------
# Copyright (c) 2016, Nicolas P. Rougier
# Distributed under the (new) BSD License.
# -----------------------------------------------------------------------------
import numpy as np
from experiment import Experiment

def session(exp):
    exp.model.setup()
    records = np.zeros((exp.n_block, exp.n_trial), dtype=exp.task.records.dtype)

    # Day 1 : GPi OFF
    g1 = exp.model["GPi:cog → THL:cog"].gain
    g2 = exp.model["GPi:mot → THL:mot"].gain
    exp.model["GPi:cog → THL:cog"].gain = 0
    exp.model["GPi:mot → THL:mot"].gain = 0
    for trial in exp.task:
        exp.model.process(exp.task, trial, model = exp.model)
    records[0] = exp.task.records

    # Day 2: GPi ON
    exp.model["GPi:cog → THL:cog"].gain = g1
    exp.model["GPi:mot → THL:mot"].gain = g2
    for trial in exp.task:
        exp.model.process(exp.task, trial, model = exp.model)
    records[1] = exp.task.records

    return records


experiment = Experiment(model = "model.json", task = "task.json",
                        result="data/theoretical/D1-off-D2-on.npy",
                        report="data/theoretical/D1-off-D2-on.txt",
                        n_session=12, n_block=2, seed=225)
records = experiment.run(session, "D1-off-D2-on")
