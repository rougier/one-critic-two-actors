This is the code accompanying the article:

"One critic, two actors: evidence for covert learning in the basal ganglia
 Meropi Topalidou, Daisuke Kase, Thomas Boraud and Nicolas P. Rougier"


### Installation

It requires python, numpy, cython and matplotlib:

```bash
$ pip install numpy cython maplotlib tqdm
```

To compile the model, just type:

```bash
$ python setup.py develop
```

### Running

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

### Figures & analysis

```bash
$ cd experiments/data
$ python output-raw-data.py
$ python figure-histograms.py
$ python figure-trials.py
$ Rscript analysis.R
```
