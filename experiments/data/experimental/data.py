import os.path
import numpy as np


data = {
    "P10-D1-saline-France": {
        'protocol': '10', 'day': 0, 'gpi': 1, 'monkey': 0,
        'sessions': [
            (0, "D1-saline-D2-muscimol/France/20150515_170052FrIB.txt"),
            (1, "D1-saline-D2-muscimol/France/20150519_182621FrIB.txt"),
            (2, "D1-saline-D2-muscimol/France/20150521_182106FrIB.txt"),
            (3, "D1-saline-D2-muscimol/France/20150525_183225FrIB.txt"),
            (4, "D1-saline-D2-muscimol/France/20150527_181154FrIB.txt")
        ]
    },
    "P10-D1-saline-Zora": {
        'protocol': '10', 'day': 0, 'gpi': 1, 'monkey': 1,
        'sessions': [
            (0, "D1-saline-D2-muscimol/Zora/20150511_184207ZIB.txt"),
            (1, "D1-saline-D2-muscimol/Zora/20150513_175700ZIB.txt"),
            (2, "D1-saline-D2-muscimol/Zora/20150518_181234ZIB.txt"),
            (3, "D1-saline-D2-muscimol/Zora/20150520_174344ZIB.txt"),
            (4, "D1-saline-D2-muscimol/Zora/20150522_184337ZIB.txt"),
            (5, "D1-saline-D2-muscimol/Zora/20150526_181854ZIB.txt")
        ]
    },
    "P10-D2-muscimol-France": {
        'protocol': '10', 'day': 1, 'gpi': 0, 'monkey': 0,
        'sessions': [
            (0, "D1-saline-D2-muscimol/France/20150516_131318FrIB.txt"),
            (1, "D1-saline-D2-muscimol/France/20150520_114127FrIB.txt"),
            (2, "D1-saline-D2-muscimol/France/20150522_150002FrIB.txt"),
            (3, "D1-saline-D2-muscimol/France/20150526_113346FrIB.txt"),
            (4, "D1-saline-D2-muscimol/France/20150528_141717FrIB.txt")
        ]
    },
    "P10-D2-muscimol-Zora": {
        'protocol': '10', 'day': 1, 'gpi': 0, 'monkey': 1,
        'sessions': [
            (0, "D1-saline-D2-muscimol/Zora/20150512_140843ZIB.txt"),
            (1, "D1-saline-D2-muscimol/Zora/20150514_143523ZIB.txt"),
            (2, "D1-saline-D2-muscimol/Zora/20150519_133552ZIB.txt"),
            (3, "D1-saline-D2-muscimol/Zora/20150521_125140ZIB.txt"),
            (4, "D1-saline-D2-muscimol/Zora/20150523_132656ZIB.txt"),
            (5, "D1-saline-D2-muscimol/Zora/20150527_145655ZIB.txt")
        ]
    },

    "P01-D1-muscimol-France": {
        'protocol': '01', 'day': 0, 'gpi': 0, 'monkey': 0,
        'sessions': [
            (0, "D1-muscimol-D2-saline/France/20150601_151258FrIB.txt"),
            (1, "D1-muscimol-D2-saline/France/20150716_162355FrIB.txt"),
            (2, "D1-muscimol-D2-saline/France/20150722_134551FrIB.txt"),
            (3, "D1-muscimol-D2-saline/France/20150728_141230FrIB.txt"),
            (4, "D1-muscimol-D2-saline/France/20150904_155756FrIB.txt")
        ]
    },
    "P01-D1-muscimol-Zora": {
        'protocol': '01', 'day': 0, 'gpi': 0, 'monkey': 1,
        'sessions': [
            (0, "D1-muscimol-D2-saline/Zora/20150601_170658ZIB.txt"),
            (1, "D1-muscimol-D2-saline/Zora/20150605_155818ZIB.txt"),
            (2, "D1-muscimol-D2-saline/Zora/20150716_163851ZIB.txt"),
            (3, "D1-muscimol-D2-saline/Zora/20150722_152159ZIB.txt"),
            (4, "D1-muscimol-D2-saline/Zora/20150728_153107ZIB.txt")
        ]
    },
    "P01-D1-muscimol-Enya": {
        'protocol': '01', 'day': 0, 'gpi': 0, 'monkey': 2,
        'sessions': [
            (0, "D1-muscimol-D2-saline/Enya/20160328_160546EnM.txt"),
            (1, "D1-muscimol-D2-saline/Enya/20160228_115055EnM.txt")
        ]
    },
    "P01-D2-saline-France": {
        'protocol': '01', 'day': 1, 'gpi': 1, 'monkey': 0,
        'sessions': [
            (0, "D1-muscimol-D2-saline/France/20150602_151454FrINB.txt"),
            (1, "D1-muscimol-D2-saline/France/20150717_165933FrINB.txt"),
            (2, "D1-muscimol-D2-saline/France/20150723_141005FrINB.txt"),
            (3, "D1-muscimol-D2-saline/France/20150729_140152FrINB.txt"),
            (4, "D1-muscimol-D2-saline/France/20150905_134635FrINB.txt")
        ]
    },
    "P01-D2-saline-Zora": {
        'protocol': '01', 'day': 1, 'gpi': 1, 'monkey': 1,
        'sessions': [
            (0, "D1-muscimol-D2-saline/Zora/20150602_155228ZINB.txt"),
            (1, "D1-muscimol-D2-saline/Zora/20150606_132301ZINB.txt"),
            (2, "D1-muscimol-D2-saline/Zora/20150717_182102ZINB.txt"),
            (3, "D1-muscimol-D2-saline/Zora/20150723_145502ZINB.txt"),
            (4, "D1-muscimol-D2-saline/Zora/20150729_144736ZINB.txt")
        ]
    },
    "P01-D2-saline-Enya": {
        'protocol': '01', 'day': 1, 'gpi': 1, 'monkey': 2,
        'sessions': [
            (0, "D1-muscimol-D2-saline/Enya/20160229_095341EnS.txt"),
            (1, "D1-muscimol-D2-saline/Enya/20160329_180726EnS.txt")
        ]
    }
}


def filter(protocol=None, monkeys=None, day=None, gpi=None):
    filenames = []
    for output, exp in data.items():
        if (protocol is None or exp['protocol'] == protocol) and \
           (monkeys is None or exp['monkey'] in monkeys) and \
           (day is None or exp['day'] == day) and \
           (gpi is None or exp['gpi'] == gpi):
            for (session_id, filename) in exp['sessions']:
                key = exp['monkey']*100 + session_id
                filenames.append((key, filename))

    # Files are sorted by monkeys first, session second
    return [f for (_, f) in sorted(filenames)]


def read(filename, ftst=1, key="good_choice"):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, filename)
    lines = [line.strip().encode() for line in open(filename).readlines()]
    R = np.recfromcsv(lines, delimiter='\t')
    # Filter out entries (ftst = ftst and num_error=0)
    I = np.argwhere((R["ftst"] == ftst) & (R["num_error"] == 0)).ravel()
    return R[I][key]


def get(protocol=None, key="success", n_trial=60,
        monkeys=None, day=None, gpi=None):
    sessions = []
    filenames = filter(protocol=protocol, monkeys=monkeys, day=day, gpi=gpi)
    for filename in filenames:
        if key == 'success':
            Z = read(filename, key='good_choice')
        elif key == 'reward':
            Z = read(filename, key='reward')
        elif key == 'cue':
            Z = read(filename, key='target_choice')
        elif key == 'RT':
            Z1 = read(filename, key='e35')
            Z2 = read(filename, key='e45')
            Z = Z2 - Z1
        else:
            raise KeyError("Unknown record key")
        if day == 0:
            sessions.append(Z[-n_trial:].tolist())
        else:
            sessions.append(Z[:n_trial].tolist())
    return sessions


def stats(Z):
    return np.mean(Z), np.std(Z), np.std(Z)/np.sqrt(len(Z))


def running_mean(Z, n=10):
    """
    Compute the running mean over a window of n trials
    Handle uneven session lengths
    """
    # Number of sessions
    n_session = len(Z)

    # Maximum session length
    length = max([len(x) for x in Z])

    # We stores all sessions into a masked array
    MT = np.ma.empty((n_session, length))
    MT.mask = True
    for i in range(len(Z)):
        MT[i, :len(Z[i])] = Z[i]

    # Mean over trials
    RM = np.zeros((n_session, 1+length-n))
    for j in range(n_session):
        for k in range(n, length+1):
            imin, imax = k-n, k
            RM[j, k-n] = np.ma.mean(MT[j, imin:imax])

    # Mean over sessions
    RM = np.ma.masked_invalid(RM)
    mean = np.ma.mean(RM, axis=0)
    std = np.ma.std(RM, axis=0)
    sem = std/np.sqrt(len(RM))
    return mean, std, sem


# ------------------------
if __name__ == '__main__':

    # Get all data on day 0 where gpi is inactive
    D1 = get(day=0, gpi=0)
    # Get all data on day 1 where gpi is active
    D2 = get(day=1, gpi=1)

    n = 10
    D1_start = [np.mean(session[:n]) for session in D1]
    D1_end   = [np.mean(session[-n:]) for session in D1]
    D2_start = [np.mean(session[:n]) for session in D2]
    D2_end   = [np.mean(session[-n:]) for session in D2]
    print(stats(D1_start))
    print(stats(D1_end))
    print(stats(D2_start))
    print(stats(D2_end))

    # Checking results using the running mean
    mean, std, sem = running_mean(D1)
    print(mean[0], std[0], sem[0])
    print(mean[-1], std[-1], sem[-1])
    mean, std, sem = running_mean(D2)
    print(mean[0], std[0], sem[0])
    print(mean[-1], std[-1], sem[-1])
        

