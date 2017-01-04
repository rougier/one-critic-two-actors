import sys
import numpy as np
from stats import stats


def display(get):
    n = 10
    
    # Get all data on day 0 where gpi is active
    D1 = get('10', day=0, gpi=1, n_trial=60, key='RT')
    # Get all data on day 1 where gpi is inactive
    D2 = get('10', day=1, gpi=0, n_trial=60, key='RT')

    D1_start = [np.mean(session[:n]) for session in D1]
    D1_end   = [np.mean(session[-n:]) for session in D1]
    D2_start = [np.mean(session[:n]) for session in D2]
    D2_end   = [np.mean(session[-n:]) for session in D2]

    print("Day 1 saline, day 2 muscimol")
    print("----------------------------")
    print("D1 start: %.3f  ±%.3f (std)  ±%.3f (sem)" % stats(D1_start))
    print("D1 end:   %.3f  ±%.3f (std)  ±%.3f (sem)" % stats(D1_end))
    print("D2 start: %.3f  ±%.3f (std)  ±%.3f (sem)" % stats(D2_start))
    print("D2 end:   %.3f  ±%.3f (std)  ±%.3f (sem)" % stats(D2_end))
    print()


    # Get all data on day 0 where gpi is inactive
    D1 = get('01', day=0, gpi=0, n_trial=60, key='RT')
    # Get all data on day 1 where gpi is active
    D2 = get('01', day=1, gpi=1, n_trial=60, key='RT')

    D1_start = [np.mean(session[:n]) for session in D1]
    D1_end   = [np.mean(session[-n:]) for session in D1]
    D2_start = [np.mean(session[:n]) for session in D2]
    D2_end   = [np.mean(session[-n:]) for session in D2]

    print("Day 2 muscimol, day 1 saline")
    print("----------------------------")
    print("D1 start: %.3f  ±%.3f (std)  ±%.3f (sem)" % stats(D1_start))
    print("D1 end:   %.3f  ±%.3f (std)  ±%.3f (sem)" % stats(D1_end))
    print("D2 start: %.3f  ±%.3f (std)  ±%.3f (sem)" % stats(D2_start))
    print("D2 end:   %.3f  ±%.3f (std)  ±%.3f (sem)" % stats(D2_end))
    print()


if __name__ == '__main__':

    from theoretical.data import get as get_theoretical
    from experimental.data import get as get_experimental

    print("Experimental results")
    print("====================")
    print()
    display(get_experimental)

    print()
    print("Theoretical results")
    print("===================")
    print()
    display(get_theoretical)
