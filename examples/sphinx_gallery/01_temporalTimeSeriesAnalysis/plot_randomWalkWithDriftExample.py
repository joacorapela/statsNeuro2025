"""
Generation of a random walk with drift time series
==================================================
"""

#%%
# Import requirements
# -------------------

import os
import numpy as np
import plotly.graph_objects as go

#%%
# Define variables
# ----------------

srate = 500
T = 2 # sec
sigma = 1.0
delta = .2
xlim = [0.9, 1.0]

#%%
# Create white noise
# ------------------
#

time = np.arange(0, T, 1.0/srate)
N = len(time)
w = np.random.normal(loc=0, scale=sigma, size=N)

#%%
# Create random walk with noise time series
# -----------------------------------------
#

rwWithDrift = np.empty(N, dtype=np.double)
rwWithDrift[0] = delta + w[0]
for i in range(1, N):
    rwWithDrift[i] = delta + - delta * rwWithDrift[i-1] + w[i]

#%%
# Plot random noise with noise time series
# ----------------------------------------
#

fig = go.Figure()
trace = go.Scatter(x=time, y=rwWithDrift, mode="lines+markers")
fig.add_trace(trace)
trace = go.Scatter(x=[0, 2], y=[0, delta*2], line=dict(dash="dot"), mode="lines+markers")
fig.add_trace(trace)
fig.update_layout(xaxis=dict(title="Time (sec)", range=xlim),
                  yaxis=dict(title="x"))

if not os.path.exists("figures"):
    os.mkdir("figures")

fig.write_html("figures/autoregressive.html")
fig.write_image("figures/autoregressive.png")

fig
