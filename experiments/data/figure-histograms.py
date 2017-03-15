import numpy as np
from matplotlib import lines
import matplotlib.pyplot as plt

def histogram(ax, D0, D1, D2, title, labels, stars):
    n = 10
    
    D0_start = [np.mean(session[:n]) for session in D0]
    D0_end = [np.mean(session[-n:]) for session in D0]
    D0_start_mean, D0_start_std, D0_start_sem = stats(D0_start)
    D0_end_mean, D0_end_std, D0_end_sem = stats(D0_end)
    D0_mean = (D0_start_mean, D0_end_mean)
    D0_sem = (D0_start_sem, D0_end_sem)
    D0_std = (D0_start_std, D0_end_std)

    D1_start = [np.mean(session[:n]) for session in D1]
    D1_end = [np.mean(session[-n:]) for session in D1]
    D1_start_mean, D1_start_std, D1_start_sem = stats(D1_start)
    D1_end_mean, D1_end_std, D1_end_sem = stats(D1_end)
    D1_mean = (D1_start_mean, D1_end_mean)
    D1_sem = (D1_start_sem, D1_end_sem)
    D1_std = (D1_start_std, D1_end_std)

    D2_start = [np.mean(session[:n]) for session in D2]
    D2_end = [np.mean(session[-n:]) for session in D2]
    D2_start_mean, D2_start_std, D2_start_sem = stats(D2_start)
    D2_end_mean, D2_end_std, D2_end_sem = stats(D2_end)
    D2_mean = (D2_start_mean, D2_end_mean)
    D2_sem = (D2_start_sem, D2_end_sem)
    D2_std = (D2_start_std, D2_end_std)

    ax.xaxis.set_tick_params(size=0)
    ax.yaxis.set_tick_params(width=1)

    # Pull the formatting out here
    bar_kw = {'width': 0.95, 'linewidth': 0, 'zorder': 5}
    err_kw = {'zorder': 10, 'fmt': 'none', 'linewidth': 0,
              'elinewidth': 1, 'ecolor': 'k'}

    def plot(X, mean, sigma, color, alpha):
        plt.bar(X+width/2.0, mean, alpha=alpha, color=color, **bar_kw)
        _, caps, _ = plt.errorbar(X+width/2.0, mean, sigma, **err_kw)

    width = 1
    index = np.array([0, 1])
    plot(index-width,     D0_mean, D0_std, '.25', 0.45)
    plot(index-width+2.5, D1_mean, D1_std, '.25', 0.45)
    plot(index-width+5.0, D2_mean, D2_std, '.25', 0.45)

    plt.xlim(-1.5, +6.5)
    plt.xticks([-0.5, 0.0, 0.5,
                2.0, 2.5, 3.0,
                4.5, 5.0, 5.5],
               ["10 first\ntrials",
                "\n\n\n%s" % labels[0],
                "10 last\ntrials",
                "10 first\ntrials",
                "\n\n\n%s" % labels[1],
                "10 last\ntrials",
                "10 first\ntrials",
                "\n\n\n%s" % labels[2],
                "10 last\ntrials"])
    plt.ylim(0.0, 1.30)
    plt.ylabel("Ratio of optimum trials")
    plt.yticks([0.00, 0.25, 0.50, 0.75, 1.00])

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')

    x, y = np.array([[-1, 1], [-0.125, -0.125]])
    ax.add_line(lines.Line2D(x, y, lw=1, color='k', clip_on=False))
    ax.add_line(lines.Line2D(x+2.5, y, lw=1, color='k', clip_on=False))
    ax.add_line(lines.Line2D(x+5.0, y, lw=1, color='k', clip_on=False))

    # Custom function to draw the diff bars
    def label_diff(X1, X2, Y, text):
        d = 0.025
        plt.plot([X1, X1, X2, X2], [Y-d, Y, Y, Y-d], color="k", lw=1)
        plt.text((X1+X2)/2.0, Y-0.015, text, transform=ax.transData,
                 va="bottom", ha="center", fontsize=20)

    label_diff(-0.5, 4.5, 1.2, stars[0])
    label_diff(2.0,  4.5, 1.1, stars[1])
    label_diff(3.0,  4.5, 1.0, stars[2])

    plt.title(title)

import scipy.stats
from stats import stats
from experimental.data import get as get_experimental
from theoretical.data import get as get_theoretical


fig = plt.figure(figsize=(12, 5), facecolor="w")

D0 = get_experimental('10', day=0, gpi=1, n_trial=60, key='success')
D1 = get_experimental('01', day=0, gpi=0, n_trial=60, key='success')
D2 = get_experimental('01', day=1, gpi=1, n_trial=60, key='success')
ax = plt.subplot(1, 2, 2)

Z = np.loadtxt("./experimental-raw-data.txt")
C0 = Z[np.where(Z[:,2]==0)][:,0]
C2 = Z[np.where(Z[:,2]==2)][:,0]
C3 = Z[np.where(Z[:,2]==3)][:,0]
C4 = Z[np.where(Z[:,2]==4)][:,0]
stars = ['*', '*', '*']

histogram(ax, D0, D1, D2, "Experimental results",
          labels = ("Control", "D1 (muscimol)", " D2 (saline)"),
          stars = stars)

D0 = get_theoretical('10', day=0, gpi=1, n_trial=60, key='success')
D1 = get_theoretical('01', day=0, gpi=0, n_trial=60, key='success')
D2 = get_theoretical('01', day=1, gpi=1, n_trial=60, key='success')
ax = plt.subplot(1, 2, 1)

Z = np.loadtxt("./theoretical-raw-data.txt")
C0 = Z[np.where(Z[:,2]==0)][:,0]
C2 = Z[np.where(Z[:,2]==2)][:,0]
C3 = Z[np.where(Z[:,2]==3)][:,0]
C4 = Z[np.where(Z[:,2]==4)][:,0]
stars = ['*', '*', '*']

histogram(ax, D0, D1, D2, "Theoretical results",
          labels = ("Control", "D1 (GPi OFF)", " D2 (GPi ON)"),
          stars = stars)

plt.tight_layout(pad=0)
plt.savefig("histogram.pdf")
plt.show()
