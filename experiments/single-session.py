# -----------------------------------------------------------------------------
# Copyright (c) 2016, Nicolas P. Rougier
# Distributed under the (new) BSD License.
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']


def plot(ax, title, text1, text2, choices, values, weights, rewards, use_weight=True, true_value=True):
    n = len(choices)
    X = np.arange(n)

    # Trials    
    ax.text(   0+1, 0.6, text1,  va="bottom", ha="left", fontsize=8)
    ax.text(n//2+1, 0.6, text2, va="bottom", ha="left", fontsize=8)

    s = 15
    
    C1 = np.argwhere(choices == 0)
    ax.scatter(X,     0.25*np.ones(n),      s=s, facecolor='0.95',  edgecolor='0.75', lw=0.5)
    ax.scatter(X[C1], 0.25*np.ones(n)[C1],  s=s, facecolor='black', edgecolor='black', lw=0.5)
    ax.text(n,      0.25, "A", va="center", ha="left")
    
    C2 = np.argwhere(choices == 1)
    ax.scatter(X,     0.00*np.ones(n),      s=s, facecolor='0.95',  edgecolor='0.75', lw=0.5)
    ax.scatter(X[C2], 0.00*np.ones(n)[C2],  s=s, facecolor='black', edgecolor='black', lw=0.5)
    ax.text(n,      0.00, "B", va="center", ha="left")
    
    R = np.argwhere(rewards == 1)
    ax.scatter(X,     0.50*np.ones(n),      s=s, facecolor=(1,.95,.95), edgecolor=(1,.75,.75), lw=0.5)
    ax.scatter(X[R],  0.50*np.ones(n)[R],   s=s, facecolor='red',  edgecolor='red', lw=0.5)
    ax.text(n,      0.50, "Reward", va="center", ha="left")
    
    ax.axvline(n//2, color="0.5", zorder=-10, lw=.5, ls="--")
    # ax.text(n//2, -0.2,  "Switch", va="top", ha="center", fontsize=8)

    # RL values
    y = 0.75

    if true_value:
        ls = "-"
    else:
        ls = ":"
        
    if values is not None:
        ax.plot(X, y+values[:,0], color=colors[0], ls=ls)
        ax.text(n, y+values[-1,0], "$V_A$", va="bottom", ha="left", color=colors[0],
                fontsize=8)
        ax.plot(X, y+values[:,1], color=colors[1], ls=ls)
        ax.text(n,  y+values[-1,1], "$V_B$", va="top", ha="left",  color=colors[1],
                fontsize=8)

        ax.text(-6, 1.25, "V=0.5", ha="left", va="bottom", color="0.5", fontsize=8)
        ax.axhline(1.25, lw=.5, color=".75", zorder=-10)

    # Hebbian weights or choices count
    y += 1
    if use_weight:
        Y0 = (weights[:,0]-weights.min())
        ax.text(n, y+Y0[-1], "$W_A$", va="bottom", ha="left", color=colors[0],
                fontsize=8)
    else:
        Y0 = np.cumsum(np.where(choices==0, 1, 0))/(n)
        ax.text(n, y+Y0[-1], "$N_A$", va="bottom", ha="left", color=colors[0],
                fontsize=8)
    ax.plot(X, y+Y0, color=colors[0])

    if use_weight:
        Y1 = (weights[:,1] - weights.min())
        ax.text(n, y+Y1[-1], "$W_B$", va="top", ha="left", color=colors[1],
                fontsize=8)
    else:
        Y1 = np.cumsum(np.where(choices==1, 1, 0))/(n)
        ax.text(n, y+Y1[-1], "$N_B$", va="top", ha="left", color=colors[1],
                fontsize=8)
    ax.plot(X, y + Y1, color=colors[1])

    if use_weight:
        ax.axhline(1.75, lw=.5, color=".75", zorder=-10)
        ax.text(-6, 1.75, "W=0.5", ha="left", va="bottom", color="0.5", fontsize=8)
    else:
        ax.axhline(1.75, lw=.5, color=".75", zorder=-10)
        ax.text(-6, 1.75, "N=0", ha="left", va="bottom", color="0.5", fontsize=8)

    ax.text(0, 2.25, title[0], ha="left", va="top", color="0.0", fontsize=10, weight="bold")
    ax.text(3, 2.25, title[1:], ha="left", va="top", color="0.0", fontsize=10)

    ax.set_xticks([])
    ax.set_yticks([])




    

if __name__ == '__main__':


    plt.figure(figsize=(10,6))
    session = 5

    from data.theoretical.data import get

    # -------------------------------------------------------------------------
    # Get all data on day 0 where gpi is active
    rewards = get('10', day=0, gpi=1, n_trial=60, key='reward')[session]
    choices = get('10', day=0, gpi=1, n_trial=60, key='cue')[session]
    values  = get('10', day=0, gpi=1, n_trial=60, key='value')[session][:,:2]
    weights = get('10', day=0, gpi=1, n_trial=60, key='CTX:cog -> CTX:ass')[session][:,:2]
    

    # Get all data on day 1 where gpi is inactive
    rewards = np.append(rewards,
                  get('10', day=1, gpi=0, n_trial=60, key='reward')[session], axis=0)
    choices = np.append(choices,
                  get('10', day=1, gpi=0, n_trial=60, key='cue')[session], axis=0)
    values = np.append(values,
                  get('10', day=1, gpi=0, n_trial=60, key='value')[session][:,:2], axis=0)
    weights = np.append(weights,
                  get('10', day=1, gpi=0, n_trial=60, key='CTX:cog -> CTX:ass')[session][:,:2], axis=0)

    
    ax = plt.subplot(2, 1, 1, frameon=False)
    choices, values, weights, rewards
    plot(ax, "A", "Day 1 - GPi ON", "Day 2 - GPi OFF",
         choices, values, weights, rewards, True)


    # -------------------------------------------------------------------------
    # Get all data on day 0 where gpi is inactive
    rewards = get('01', day=0, gpi=0, n_trial=60, key='reward')[session]
    choices = get('01', day=0, gpi=0, n_trial=60, key='cue')[session]
    values  = get('01', day=0, gpi=0, n_trial=60, key='value')[session][:,:2]
    weights = get('01', day=0, gpi=0, n_trial=60, key='CTX:cog -> CTX:ass')[session][:,:2]

    # Get all data on day 1 where gpi is inactive
    rewards = np.append(rewards,
                  get('01', day=1, gpi=1, n_trial=60, key='reward')[session], axis=0)
    choices = np.append(choices,
                  get('01', day=1, gpi=1, n_trial=60, key='cue')[session], axis=0)
    values = np.append(values,
                  get('01', day=1, gpi=1, n_trial=60, key='value')[session][:,:2], axis=0)
    weights = np.append(weights,
                  get('01', day=1, gpi=1, n_trial=60, key='CTX:cog -> CTX:ass')[session][:,:2], axis=0)

    ax = plt.subplot(2, 1, 2, frameon=False)
    plot(ax, "B", "Day 1 - GPi OFF", "Day 2 - GPi ON",
         choices, values, weights, rewards, True)




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

    
    from data.experimental.data import get

    # -------------------------------------------------------------------------
    # Get all data on day 0 where gpi is active
    session = 8
    rewards = get('10', day=0, gpi=1, n_trial=60, key='reward')[session]
    choices = get('10', day=0, gpi=1, n_trial=60, key='cue')[session]

    # Get all data on day 1 where gpi is inactive
    rewards = np.append(rewards,
                  get('10', day=1, gpi=0, n_trial=60, key='reward')[session], axis=0)
    choices = np.append(choices,
                  get('10', day=1, gpi=0, n_trial=60, key='cue')[session], axis=0)
    choices = np.where(choices==b'A', 0, 1)
    values = .25/2 + .75*compute_values(choices, rewards)
    
    ax = plt.subplot(4, 1, 3, frameon=False)
    plot(ax, "C (primates, session #%d)" % session, "Day 1 - Saline", "Day 2 - Muscimol",
         choices, values, None, rewards, False, False)


    # -------------------------------------------------------------------------
    # Get all data on day 0 where gpi is inactive
    session = 5
    rewards = get('01', day=0, gpi=0, n_trial=60, key='reward')[session]
    choices = get('01', day=0, gpi=0, n_trial=60, key='cue')[session]

    # Get all data on day 1 where gpi is active
    rewards = np.append(rewards,
                  get('01', day=1, gpi=1, n_trial=60, key='reward')[session], axis=0)
    choices = np.append(choices,
                  get('01', day=1, gpi=1, n_trial=60, key='cue')[session], axis=0)
    choices = np.where(choices==b'A', 0, 1)
    values = .25/2 + .75*compute_values(choices, rewards)
    
    ax = plt.subplot(4, 1, 4, frameon=False)
    plot(ax, "D (primates, session #%d)" % session, "Day 1 - Muscimol", "Day 2 - Saline",
         choices, values, None, rewards, False, False)

    plt.savefig("single-session.pdf")
    plt.show()
