# -----------------------------------------------------------------------------
# Copyright (c) 2016, Nicolas P. Rougier
# Distributed under the (new) BSD License.
# -----------------------------------------------------------------------------
import random
import tqdm
import numpy as np
import matplotlib.pyplot as plt
from task import Task
from model import Model

colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

def plot_freq(ax, ctx, thl, gpi, stn, str, i0, i1, duration, dt, title, xlabel, ylabel):
    timesteps = np.linspace(0, duration, duration/dt)
    stn = stn[:duration:dt]
    str = str[:duration:dt]
    ctx = ctx[:duration:dt]
    gpi = gpi[:duration:dt]
    thl = thl[:duration:dt]

    fontsize = 8

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    
    x = np.argwhere((ctx[:,i0] - ctx[:,i1]) > 40)[0] * dt
    ax.text(x, -6, "↑\nDecision", fontsize=8, va="top", ha="center")
    ax.text(500, -6, "↑\nTrial start", fontsize=8, va="top", ha="center")
    
    ax.plot(timesteps, ctx[:,i1], c=colors[0], ls="--")
    ax.plot(timesteps, ctx[:,i0], c=colors[0])
    ax.text(duration, ctx[-1,i0]+1, "CTX", fontsize=fontsize, # weight="bold",
            transform=ax.transData, va="bottom", ha="right", color=colors[0])

    ax.plot(timesteps, gpi[:,i1], c=colors[1], ls="--")
    ax.plot(timesteps, gpi[:,i0], c=colors[1])
    ax.text(duration, gpi[-1,i0]-1, "GPi", fontsize=fontsize, # weight="bold",
            transform=ax.transData, va="top", ha="right", color=colors[1])

    ax.plot(timesteps, thl[:,i1], c=colors[2], ls="--")
    ax.plot(timesteps, thl[:,i0], c=colors[2])
    ax.text(duration, thl[-1,i0]+1, "THL", fontsize=fontsize, # weight="bold",
            transform=ax.transData, va="bottom", ha="right", color=colors[2])

    ax.plot(timesteps, stn[:,i1], c=colors[3], ls="--")
    ax.plot(timesteps, stn[:,i0], c=colors[3])
    ax.text(duration, stn[-1,i0]+1, "STN", fontsize=fontsize, # weight="bold",
            transform=ax.transData, va="bottom", ha="right", color=colors[3])

    ax.plot(timesteps, str[:,i1], c=colors[4], ls="--")
    ax.plot(timesteps, str[:,i0], c=colors[4])
    ax.text(duration, str[-1,i0]+1, "STR", fontsize=fontsize, # weight="bold",
            transform=ax.transData, va="bottom", ha="right", color=colors[4])

    ax.text(0.025, 0.95, title[0], fontsize=10, weight="bold", va="center",
            transform=ax.transAxes, color="black")
    ax.text(0.055, 0.95, title[1:], fontsize=10, weight="normal", va="center",
            transform=ax.transAxes, color="black")

    if xlabel:
        ax.set_xlabel("Time (ms)")
    if ylabel:
        ax.set_ylabel("Firing rate (spikes/s)")
    ax.set_xticks([0,2000])
    ax.set_ylim(-5,145)
    ax.set_yticks([0,40,80,120])


def spikegen(fr, dt, n=10):
    S = []
    for i in range(n):
        I = np.argwhere(np.random.uniform(0,1000,len(fr)) < fr*dt).ravel()
        S.append(I*dt)
    return S

def plot_raster(ax, ctx, thl, gpi, stn, str, i0, i1, duration, dt, title):
    def plot_scatter(X, y, color):
        Y = y*np.ones(len(X))
        ax.scatter(X, Y, s=.5, marker='|', facecolor=color, edgecolor="none")

    timesteps = np.linspace(0, duration, duration/dt)
    stn = stn[:duration:dt]
    str = str[:duration:dt]
    ctx = ctx[:duration:dt]
    gpi = gpi[:duration:dt]
    thl = thl[:duration:dt]

    n = 10
    y = 100
    
    S = spikegen(ctx[:,i0], dt=dt, n=n)
    for i in range(n): plot_scatter(S[i], y+i, colors[0])
    y += n+2
    S = spikegen(ctx[:,i1], dt=dt, n=n)
    for i in range(n): plot_scatter(S[i], y+i, colors[0])
    y += n+1
    ax.text(duration, y, "Cortex channels", ha="right", va="bottom", fontsize=7,
            color=colors[0])
    

    # S = spikegen(gpi[:,i0], dt=dt, n=n)
    # for i in range(n): plot_scatter(S[i], y+i, colors[1])
    # y += n
    # S = spikegen(gpi[:,i1], dt=dt, n=n)
    # for i in range(n): plot_scatter(S[i], y+i, colors[1])
    # y += n+1

    # S = spikegen(thl[:,i0], dt=dt, n=n)
    # for i in range(n): plot_scatter(S[i], y+i, colors[2])
    # y += n
    # S = spikegen(thl[:,i1], dt=dt, n=n)
    # for i in range(n): plot_scatter(S[i], y+i, colors[2])
    # y += n+1

    # S = spikegen(stn[:,i0], dt=dt, n=n)
    # for i in range(n): plot_scatter(S[i], y+i, colors[3])
    # y += n
    # S = spikegen(stn[:,i1], dt=dt, n=n)
    # for i in range(n): plot_scatter(S[i], y+i, colors[3])
    # y += n+1

    # S = spikegen(str[:,i0], dt=dt, n=n)
    # for i in range(n): plot_scatter(S[i], y+i, colors[4])
    # y += n
    # S = spikegen(str[:,i1], dt=dt, n=n)
    # for i in range(n): plot_scatter(S[i], y+i, colors[4])
    # y += n+1

                    


def setup(task_filename="task.json", model_filename="model.json"):
    seed = 123
    np.random.seed(seed)
    random.seed(seed)
    model = Model(model_filename)
    task = Task(task_filename)
    #if learn:
    #    for trial in tqdm.tqdm(task):
    #        model.process(task, trial, stop=False, debug=False)
    return task, model


def simulate(task, model, loop, gpi=0):
    if not gpi:
        model["GPi:cog → THL:cog"].gain = 0
        model["GPi:mot → THL:mot"].gain = 0
    trial = task[4]
    model.process(task, trial, stop=False, debug=False)
    
    stn = model["STN"][loop].history #[:duration:10]
    str = model["STR"][loop].history #[:duration:10]
    ctx = model["CTX"][loop].history #[:duration:10]
    gpi = model["GPi"][loop].history #[:duration:10]
    thl = model["THL"][loop].history #[:duration:10]

    duration = 2000
    i0, i1 = trial[loop].nonzero()[0]
    if ctx[duration,i0] < ctx[duration,i1]:
        i0, i1 = i1, i0
    return ctx, thl, gpi, stn, str, i0, i1
    


dt = 10
duration = 2000

fig = plt.figure(figsize=(6,10))

task, model = setup("task.json", "model-guthrie.json")

ax = plt.subplot(3,1,1)
ctx, thl, gpi, stn, str, i0, i1 = simulate(task, model, "mot", 1)
plot_freq(ax, ctx, thl, gpi, stn, str, i0, i1, duration, dt,
          "A Motor channel (no cortical competition)", 0, 1)
plot_raster(ax, ctx, thl, gpi, stn, str, i0, i1, duration, dt, "")

task, model = setup("task.json", "model-noisy.json")

ax = plt.subplot(3,1,3)
ctx, thl, gpi, stn, str, i0, i1 = simulate(task, model, "mot", 1)
plot_freq(ax, ctx, thl, gpi, stn, str, i0, i1, duration, dt,
          "C Motor channel", 1, 1)
plot_raster(ax, ctx, thl, gpi, stn, str, i0, i1, duration, dt, "")

ax = plt.subplot(3,1,2)
ctx, thl, gpi, stn, str, i0, i1 = simulate(task, model, "mot", 0)
plot_freq(ax, ctx, thl, gpi, stn, str, i0, i1, duration, dt,
          "B Motor channel (no basal competition)", 0, 1)
plot_raster(ax, ctx, thl, gpi, stn, str, i0, i1, duration, dt, "")


plt.tight_layout()
plt.savefig("single-trial-motor.pdf")
plt.show()
