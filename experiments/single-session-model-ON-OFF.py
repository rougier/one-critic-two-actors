# -----------------------------------------------------------------------------
# Copyright (c) 2016, Nicolas P. Rougier
# Distributed under the (new) BSD License.
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']


def plot(axs, title, text1, text2, choices, values, weights, rewards, use_weight=True, true_value=True):
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
    ax1.text(0.01, 1, "Weight",  va="top", ha="left", fontsize=10,
             transform=ax1.transAxes)
    ax2.text(0.01, 1, "Value",  va="top", ha="left", fontsize=10,
             transform=ax2.transAxes)
#    ax3.text(0.1, 1, "Value",  va="top", ha="left", fontsize=10,
#             transform=ax1.transAxes)
    
    # Trials    
    #ax.text(   0+1, 0.6, text1,  va="bottom", ha="left", fontsize=8)
    #ax.text(n//2+1, 0.6, text2, va="bottom", ha="left", fontsize=8)

    s = 50
    
    C1 = np.argwhere(choices == 0)
    ax3.scatter(X,     3*np.ones(n),      s=s, facecolor='0.95',  edgecolor='0.75', lw=0.5)
    ax3.scatter(X[C1], 3*np.ones(n)[C1],  s=s, facecolor=colors[0], edgecolor=colors[0], lw=0.5)
    # ax3.text(n,      0.25, "A", va="center", ha="left")
    
    C2 = np.argwhere(choices == 1)
    ax3.scatter(X,     2*np.ones(n),      s=s, facecolor='0.95',  edgecolor='0.75', lw=0.5)
    ax3.scatter(X[C2], 2*np.ones(n)[C2],  s=s, facecolor=colors[1], edgecolor=colors[1], lw=0.5)
    # ax3.text(n,      0.00, "B", va="center", ha="left")
    
    R = np.argwhere(rewards == 1)
    ax3.scatter(X,     1*np.ones(n),      s=s, facecolor=(1,.95,.95), edgecolor=(1,.75,.75), lw=0.5)
    ax3.scatter(X[R],  1*np.ones(n)[R],   s=s, facecolor='red',  edgecolor='red', lw=0.5)

    ax3.set_ylim(0.5,3.5)
    
    # ax3.text(n,      0.50, "Reward", va="center", ha="left")
    
    # ax.axvline(n//2, color="0.5", zorder=-10, lw=.5, ls="--")
    # ax.text(n//2, -0.2,  "Switch", va="top", ha="center", fontsize=8)

    # RL values
    y = 0.75

    if true_value:
        ls = "-"
    else:
        ls = ":"
        
    #if values is not None:
    ax2.plot(X, values[:,0], color=colors[0])
    #ax.text(n, y+values[-1,0], "$V_A$", va="bottom", ha="left", color=colors[0],
    #        fontsize=8)
    ax2.plot(X, values[:,1], color=colors[1])

    ax2.set_ylim(0.25,0.75)
    
    #ax.text(n,  y+values[-1,1], "$V_B$", va="top", ha="left",  color=colors[1],
    #            fontsize=8)
    #ax.text(-6, 1.25, "V=0.5", ha="left", va="bottom", color="0.5", fontsize=8)
    #    ax.axhline(1.25, lw=.5, color=".75", zorder=-10)

    # Hebbian weights or choices count
    #y += 1
    #if use_weight:
    Y0 = weights[:,0]
    #ax.text(n, y+Y0[-1], "$W_A$", va="bottom", ha="left", color=colors[0],
    #        fontsize=8)
    ax1.plot(X, Y0, color=colors[0])

    Y1 = weights[:,1]
    ##ax.text(n, y+Y1[-1], "$W_B$", va="top", ha="left", color=colors[1],
#            fontsize=8)
    ax1.plot(X, Y1, color=colors[1])

    ax1.set_ylim(0.450,0.650)
    
#    if use_weight:
#        ax.axhline(1.75, lw=.5, color=".75", zorder=-10)
#        ax.text(-6, 1.75, "W=0.5", ha="left", va="bottom", color="0.5", fontsize=8)
#    else:
#        ax.axhline(1.75, lw=.5, color=".75", zorder=-10)
#        ax.text(-6, 1.75, "N=0", ha="left", va="bottom", color="0.5", fontsize=8)

 #   ax.text(0, 2.25, title[0], ha="left", va="top", color="0.0", fontsize=10, weight="bold")
 #   ax.text(3, 2.25, title[1:], ha="left", va="top", color="0.0", fontsize=10)

 #   ax.set_xticks([])
 #   ax.set_yticks([])




    

if __name__ == '__main__':


    plt.figure(figsize=(8,8))
    session = 5

    from data.theoretical.data import get

    # -------------------------------------------------------------------------
    # Get all data on day 0 where gpi is active
    rewards = get('10', day=0, gpi=1, n_trial=60, key='reward')[session]
    choices = get('10', day=0, gpi=1, n_trial=60, key='cue')[session]
    values  = get('10', day=0, gpi=1, n_trial=60, key='value')[session][:,:2]
    weights = get('10', day=0, gpi=1, n_trial=60, key='CTX:cog -> CTX:ass')[session][:,:2]
    

    # Get all data on day 1 where gpi is inactive
    #rewards = np.append(rewards,
    #              get('10', day=1, gpi=0, n_trial=60, key='reward')[session], axis=0)
    #choices = np.append(choices,
    #              get('10', day=1, gpi=0, n_trial=60, key='cue')[session], axis=0)
    #values = np.append(values,
    #              get('10', day=1, gpi=0, n_trial=60, key='value')[session][:,:2], axis=0)
    #weights = np.append(weights,
    #              get('10', day=1, gpi=0, n_trial=60, key='CTX:cog -> CTX:ass')[session][:,:2], axis=0)

    plt.subplots_adjust(hspace=0.05)
    ax1 = plt.subplot(6, 1, 1)
    ax2 = plt.subplot(6, 1, 2, sharex=ax1)
    ax3 = plt.subplot(6, 1, 3, sharex=ax1, frameon=False)
    plot((ax1,ax2,ax3),
         "A", "Day 1 - GPi ON", "Day 2 - GPi OFF",
         choices, values, weights, rewards, True)
    

    # -------------------------------------------------------------------------
    # Get all data on day 0 where gpi is inactive
    rewards = get('01', day=0, gpi=0, n_trial=60, key='reward')[session]
    choices = get('01', day=0, gpi=0, n_trial=60, key='cue')[session]
    values  = get('01', day=0, gpi=0, n_trial=60, key='value')[session][:,:2]
    weights = get('01', day=0, gpi=0, n_trial=60, key='CTX:cog -> CTX:ass')[session][:,:2]

    # Get all data on day 1 where gpi is inactive
    #rewards = np.append(rewards,
    #              get('01', day=1, gpi=1, n_trial=60, key='reward')[session], axis=0)
    #choices = np.append(choices,
    #              get('01', day=1, gpi=1, n_trial=60, key='cue')[session], axis=0)
    #values = np.append(values,
    #              get('01', day=1, gpi=1, n_trial=60, key='value')[session][:,:2], axis=0)
    #weights = np.append(weights,
    #              get('01', day=1, gpi=1, n_trial=60, key='CTX:cog -> CTX:ass')[session][:,:2], axis=0)

    ax1 = plt.subplot(6, 1, 4)
    ax2 = plt.subplot(6, 1, 5, sharex=ax1)
    ax3 = plt.subplot(6, 1, 6, sharex=ax1, frameon=False)
    # ax = plt.subplot(2, 1, 2, frameon=False)
    plot((ax1,ax2,ax3),
         "B", "Day 1 - GPi OFF", "Day 2 - GPi ON",
         choices, values, weights, rewards, True)

    plt.savefig("single-session-model-ON-OFF.pdf")
    plt.show()
