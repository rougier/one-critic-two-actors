import time
from theoretical.data import get as get_theoretical
from experimental.data import get as get_experimental


def write_data(get, filename):
    n = 10
    D0 = get('10', day=0, gpi=1, n_trial=60, key='success')
    D1 = get('01', day=0, gpi=0, n_trial=60, key='success')
    D2 = get('01', day=1, gpi=1, n_trial=60, key='success')

    condition_0 = 0  # Control / Saline / 10 firsts
    condition_1 = 1  # Control / Saline / 10 lasts
    condition_2 = 2  # Day 1 / Muscimol / 10 firsts
    condition_3 = 3  # Day 1 / Muscimol / 10 lasts
    condition_4 = 4  # Day 2 / Saline / 10 firsts
    condition_5 = 5  # Day 2 / Saline / 10 lasts

    file = open(filename, "w")
    file.write("# File: %s\n" % filename)
    file.write("# Date: %s\n" % time.asctime())
    file.write("# Author: Nicolas P. Rougier <Nicolas.Rougier@inria.fr>\n")
    file.write("# Fields: performance\tsession_id\tcondition\n")
    file.write("# condition = 0: Control / Saline / 10 firsts\n")
    file.write("# condition = 1: Control / Saline / 10 lasts\n")
    file.write("# condition = 2: Day 1 / Muscimol / 10 firsts\n")
    file.write("# condition = 3: Day 1 / Muscimol / 10 lasts\n")
    file.write("# condition = 4: Day 2 / Saline / 10 firsts\n")
    file.write("# condition = 5: Day 2 / Saline / 10 lasts\n")

    
    for session_id, session in enumerate(D0):
        for trial in session[:n]:
            file.write("%d\t%d\t%d\n" % (int(trial), session_id, condition_0))
        for trial in session[-n:]:
            file.write("%d\t%d\t%d\n" % (int(trial), session_id, condition_1))

    for session_id, session in enumerate(D1):
        for trial in session[:n]:
            file.write("%d\t%d\t%d\n" % (int(trial), session_id, condition_2))
        for trial in session[-n:]:
            file.write("%d\t%d\t%d\n" % (int(trial), session_id, condition_3))

    for session_id, session in enumerate(D2):
        for trial in session[:n]:
            file.write("%d\t%d\t%d\n" % (int(trial), session_id, condition_4))
        for trial in session[-n:]:
            file.write("%d\t%d\t%d\n" % (int(trial), session_id, condition_5))
    file.close()

write_data(get_theoretical, "theoretical-raw-data.txt")
write_data(get_experimental, "experimental-raw-data.txt")
