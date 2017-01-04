# Installation

It requires python, numpy, cython and matplotlib:

```bash
$ pip install numpy cython maplotlib tqdm
```

To compile the model, just type:

```bash
$ python setup.py develop
```

Then you can run a single trial:

```bash
$ cd experiments
$ python single-trial.py
```

Or the full version:

```bash
$ cd experiments
$ python experiment-D1-on-D2-on.py
$ python experiment-D1-off-D2-on.py
$ python experiment-D1-on-D2-off.py
```
