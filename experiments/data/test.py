import numpy as np
from experimental.data import get

D1 = get('01', day=0, gpi=0, n_trial=60, key='success')
D2 = get('01', day=1, gpi=1, n_trial=60, key='success')

# 1: Day 1, start
# 2: Day 1, end
# 3: Day 2, start
# 4: Day 2, end


data = []
groups = []

for i, session in enumerate(D1):
    for trial in session[:10]:
        # print(trial, i, 1)
        data.append(trial)
        groups.append(1)
    for trial in session[-10:]:
        # print(trial, i, 2)
        data.append(trial)
        groups.append(2)

for i, session in enumerate(D2):
    for trial in session[:10]:
        # print(trial, i, 3)
        data.append(trial)
        groups.append(3)
    for trial in session[-10:]:
        # print(trial, i, 4)
        data.append(trial)
        groups.append(4)

data = np.array(data)
groups = np.array(groups)

from statsmodels.stats.multicomp import MultiComparison
print(MultiComparison(data, groups).tukeyhsd())
