import os.path
import numpy as np

data = {
    "P01-D1": {
        'protocol': '01', 'day': 0, 'gpi': 0,
        'filename': 'D1-off-D2-on.npy',
    },
    "P01-D2": {
        'protocol': '01', 'day': 1, 'gpi': 1,
        'filename': 'D1-off-D2-on.npy',
    },
    "P10-D1": {
        'protocol': '10', 'day': 0, 'gpi': 1,
        'filename': 'D1-on-D2-off.npy',
    },
    "P10-D2": {
        'protocol': '10', 'day': 1, 'gpi': 0,
        'filename': 'D1-on-D2-off.npy',
    },
    "P11-D1": {
        'protocol': '11', 'day': 0, 'gpi': 1,
        'filename': 'D1-on-D2-on.npy',
    },
    "P11-D2": {
        'protocol': '11', 'day': 1, 'gpi': 1,
        'filename': 'D1-on-D2-on.npy',
    },
}


def get(protocol=None, key="success", n_trial=60,
        monkeys=None, day=None, gpi=None):

    dirname = os.path.dirname(__file__)

    if key == "success":
        key = "best"
    elif key == "RT":
        key = "RT"
#    else:
#        raise KeyError("Unknown record key")

    sessions = []
    for output, exp in data.items():
        if (protocol is None or exp['protocol'] == protocol) and \
           (day is None or exp['day'] == day) and \
           (gpi is None or exp['gpi'] == gpi):
            filename = os.path.join(dirname, exp['filename'])
            Z = np.load(filename)
            for session in Z[:, day, :][key]:
                sessions.append(session)
    return sessions

