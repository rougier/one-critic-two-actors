# -----------------------------------------------------------------------------
# Copyright (c) 2016, Nicolas P. Rougier
# Distributed under the (new) BSD License.
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']


def plot(axs, title, choices, values, weights, rewards):
    n = len(choices)
    X = np.arange(n)

    ax1, ax2, ax3 = axs
    ax2.set_xticks([])
    ax3.set_xticks([])

    for ax in axs:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
        ax.set_xlim(-0.5,len(choices)-0.5)

    ax1.spines['bottom'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    ax3.spines['bottom'].set_visible(False)

    ax3.set_yticks([1,2,3])
    ax3.set_yticklabels(["Rew.", "A", "B"])

    ax1.text(1, 1, title,  va="top", ha="right", fontsize=16, weight="bold",
             transform=ax1.transAxes)
    ax1.text(0.01, 1, "Cumulated choice count",  va="top", ha="left", fontsize=10,
             transform=ax1.transAxes)
    ax2.text(0.01, 1, "Estimated value",  va="top", ha="left", fontsize=10,
             transform=ax2.transAxes)

    
    s = 50
    
    C1 = np.argwhere(choices == 0)
    ax3.scatter(X,     3*np.ones(n),      s=s, facecolor='0.95',  edgecolor='0.75', lw=0.5)
    ax3.scatter(X[C1], 3*np.ones(n)[C1],  s=s, facecolor=colors[0], edgecolor=colors[0], lw=0.5)
    
    C2 = np.argwhere(choices == 1)
    ax3.scatter(X,     2*np.ones(n),      s=s, facecolor='0.95',  edgecolor='0.75', lw=0.5)
    ax3.scatter(X[C2], 2*np.ones(n)[C2],  s=s, facecolor=colors[1], edgecolor=colors[1], lw=0.5)
    
    R = np.argwhere(rewards == 1)
    ax3.scatter(X,     1*np.ones(n),      s=s, facecolor=(1,.95,.95), edgecolor=(1,.75,.75), lw=0.5)
    ax3.scatter(X[R],  1*np.ones(n)[R],   s=s, facecolor='red',  edgecolor='red', lw=0.5)

    ax3.set_ylim(0.5,3.5)

    ax2.plot(X, values[:,0], color=colors[0])
    ax2.plot(X, values[:,1], color=colors[1])
    ax2.set_ylim(-0.1,1.1)

    Y0 = weights[:,0]
    ax1.plot(X, Y0, color=colors[0])

    Y1 = weights[:,1]
    ax1.plot(X, Y1, color=colors[1])
    ax1.set_ylim(-1,41)


def compute_weights(choices):
    weights = np.zeros((len(rewards),2))
    sum_c0, sum_c1 = 0, 0
    for i,choice in enumerate(choices):
        if choice == 0:
            sum_c0 += 1
        elif choice == 1:
            sum_c1 += 1
        weights[i,0] = sum_c0
        weights[i,1] = sum_c1
    return weights
        
def compute_values(choices, rewards):
    values = np.zeros((len(rewards),2))
    sum_r0, sum_c0 = 0, 0
    sum_r1, sum_c1 = 0, 0
    index = 0
    for choice, reward in zip(choices, rewards):
        if choice == 0:
            sum_c0 += 1
            sum_r0 += reward
        else:
            sum_c1 += 1
            sum_r1 += reward

        if not sum_c0:
            values[index,0] = 0
        else:
            values[index,0] = sum_r0/sum_c0
        if not sum_c1:
            values[index,1] = 0
        else:
            values[index,1] = sum_r1/sum_c1
        index += 1
    return values

if __name__ == '__main__':


    plt.figure(figsize=(8,8))
    session = 5

    from data.experimental.data import get


    # -------------------------------------------------------------------------
    # Get all data on day 0 where gpi is active
    session = 9
    rewards = np.array(get('10', day=0, gpi=1, n_trial=60, key='reward')[session])
    choices = get('10', day=0, gpi=1, n_trial=60, key='cue')[session]
    choices = np.where(np.array(choices)==b'A', 0, 1)
    values = compute_values(choices, rewards)
    weights = compute_weights(choices)
    print(weights[-1])

    
    plt.subplots_adjust(hspace=0.05)
    ax1 = plt.subplot(6, 1, 1)
    ax2 = plt.subplot(6, 1, 2, sharex=ax1)
    ax3 = plt.subplot(6, 1, 3, sharex=ax1, frameon=False)
    plot((ax1,ax2,ax3), "A", choices, values, weights, rewards)
    

    # -------------------------------------------------------------------------
    # Get all data on day 0 where gpi is active
    session = 5
    rewards = np.array(get('01', day=0, gpi=0, n_trial=60, key='reward')[session])
    choices = get('01', day=0, gpi=0, n_trial=60, key='cue')[session]
    choices = np.where(np.array(choices)==b'A', 0, 1)
    values = compute_values(choices, rewards)
    weights = compute_weights(choices)

    ax1 = plt.subplot(6, 1, 4)
    ax2 = plt.subplot(6, 1, 5, sharex=ax1)
    ax3 = plt.subplot(6, 1, 6, sharex=ax1, frameon=False)
    plot((ax1,ax2,ax3), "B", choices, values, weights, rewards)

    plt.savefig("single-session-monkey-ON-OFF.pdf")
    plt.show()
