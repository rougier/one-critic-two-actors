import numpy as np


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
