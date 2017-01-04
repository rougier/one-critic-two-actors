import numpy as np
from stats import running_mean
import matplotlib.pyplot as plt

markersize = 50

def subplot(*args, **kwargs):
    ax = plt.subplot(*args, **kwargs)
    ax.patch.set_facecolor("w")
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    # ax.spines['bottom'].set_color('none')
    ax.yaxis.set_ticks_position('left')
    ax.yaxis.set_tick_params(direction="out")
    ax.xaxis.set_ticks_position('bottom')
    ax.xaxis.set_tick_params(direction="out")
    return ax


def plot_trials(ax, sessions):

    n_mean = 10
    n_trial = max([len(session) for session in sessions])

    y = 1
    ax.axhline(y-0.5, linewidth=0.5, linestyle="--", color='k', alpha=.5)

    for session in sessions:
        session = np.array(session)
        X = np.arange(n_trial)
        X0 = 1+X[np.argwhere(1-session)]
        X1 = 1+X[np.argwhere(session)]
        Y = y*np.ones(len(X0))
        ax.scatter(X0, Y, s=markersize, color="w", edgecolor="k", lw=.25)
        Y = y*np.ones(len(X1))
        ax.scatter(X1, Y, s=markersize, color="k", edgecolor="k", lw=.25)
        y += 1

    x0, x1 = 0.5, n_mean+.5,
    ax.axvspan(x0, x1, facecolor='0.95', edgecolor="none", zorder=-10)
    ax.text(x0+(x1-x0)/2, 0.25, "10 first trials",
            ha='center', va='top', transform=ax.transData)

    x0, x1 = n_trial-n_mean+0.5, n_trial+0.5,
    ax.axvspan(x0, x1, facecolor='0.95', edgecolor="none", zorder=-10)
    ax.text(x0+(x1-x0)/2, 0.25, "10 last trials",
            ha='center', va='top', transform=ax.transData)
    ax.set_xlim(0, n_trial+0.5)
    ax.set_ylim(0.5, y-0.5)
    ax.set_yticks(np.arange(y)[1:])
    ax.set_xticks([])


def plot_mean_performance(ax, sessions):
    n = 10
    n_trial = max([len(session) for session in sessions])

    
    M, STD, SEM = running_mean(sessions, n=n)
    X = np.arange(n, n+len(M))
    ax.plot(X, M, linewidth=2, color='k')

    text = ax.text(X[0]-0.5, M[0], "%.2f" % M[0], fontsize=10,
                   ha='right', va='center', transform=ax.transData)
    text.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.75))
    text = ax.text(X[-1]+0.1, M[-1], "%.2f" % M[-1], fontsize=10,
                   ha='left', va='center', transform=ax.transData)
    # text.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))
    ax.plot(X, M+SEM, linewidth=.5, linestyle='-', color='.75')
    ax.plot(X, M-SEM, linewidth=.5, linestyle='-', color='.75')
    ax.fill_between(X, M+SEM, M-SEM, color='k', alpha=0.05)

    ax.fill([0, 0, 10, 10], [0, 1, 1, 0], fill=False, hatch='//', color='.5')
    ax.axhline(0.25, linewidth=0.5, color='k', alpha=.5, ls=':')
    ax.axhline(0.5, linewidth=0.5, color='k', alpha=.5, ls=':')
    ax.axhline(0.75, linewidth=0.5, color='k', alpha=.5, ls=':')
    ax.axhline(1.0, linewidth=0.5, color='k', alpha=.5, ls=':')
    ax.set_ylim(0, 1.01)
#    ax.set_xlim(-0.5, n_trial)

    
def figure(D1, D2, label, output):

    plt.figure(figsize=(16, 8), facecolor='w')

    ax = subplot(2, 2, 1)
    plot_trials(ax, D1)
    ax.set_xlabel(label[0])
    ax.set_ylabel("Session #")
    ax = subplot(2, 2, 2)
    plot_trials(ax, D2)
    ax.set_xlabel(label[1])
    ax.set_yticks([])

    ax = subplot(2, 2, 3)
    plot_mean_performance(ax, D1)
    ax.set_yticks([0.0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xlabel(label[0])
    ax.set_ylabel("Mean success rate")

    ax = subplot(2, 2, 4)
    plot_mean_performance(ax, D2)
    ax.set_yticks([])
    ax.set_xlabel(label[1])

    plt.tight_layout()
    plt.savefig(output)




if __name__ == '__main__':
    from experimental.data import get as get_experimental

    D1 = get_experimental('01', day=0, gpi=0, n_trial=60, key='success')
    D2 = get_experimental('01', day=1, gpi=1, n_trial=60, key='success')
    figure(D1, D2, ["D1 (muscimol)", "D2 (saline)"], "experimental-01.pdf")

    D1 = get_experimental('10', day=0, gpi=1, n_trial=60, key='success')
    D2 = get_experimental('10', day=1, gpi=0, n_trial=60, key='success')
    figure(D1, D2, ["D1 (saline)", "D2 (muscimol)"], "experimental-10.pdf")

    plt.show()

    from theoretical.data import get as get_theoretical

    D1 = get_theoretical('01', day=0, gpi=0, n_trial=60, key='success')
    D2 = get_theoretical('01', day=1, gpi=1, n_trial=60, key='success')
    figure(D1, D2, ["D1 (GPi OFF)", "D2 (GPi ON)"], "theoretical-01.pdf")

    D1 = get_theoretical('10', day=0, gpi=1, n_trial=60, key='success')
    D2 = get_theoretical('10', day=1, gpi=0, n_trial=60, key='success')
    figure(D1, D2, ["D1 (GPi ON)", "D2 (GPi OFF)"], "theoretical-10.pdf")
    
    D1 = get_theoretical('11', day=0, gpi=1, n_trial=60, key='success')
    D2 = get_theoretical('11', day=1, gpi=1, n_trial=60, key='success')
    figure(D1, D2, ["D1 (GPi ON)", "D2 (GPi ON)"], "theoretical-11.pdf")

    plt.show()
