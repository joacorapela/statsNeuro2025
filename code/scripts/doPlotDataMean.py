import sys
import argparse
import numpy as np
import scipy.io
import plotly.graph_objects as go


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--channel_label", type=str, help="channels label",
                        default="Cz")
    parser.add_argument("--data_filename", type=str, help="data filename",
                        default="../../../data/D_01_cleaned.mat")
    args = parser.parse_args()

    channel_label = args.channel_label
    data_filename = args.data_filename

    mat = scipy.io.loadmat(data_filename)
    data = mat["data"]
    times = mat["times"].flatten().tolist()
    n_channels = len(mat["chanlabels"][0])

    # get channel labels
    chanlabels = [None] * n_channels
    for i in range(n_channels):
        chanlabels[i] = mat["chanlabels"][0][i][0]

    channel_index = chanlabels.index(channel_label)

    fig = go.Figure()
    channel_data = data[channel_index, :, :]
    channel_mean = np.mean(channel_data, axis=1)

    trace = go.Scatter(x=times, y=channel_mean, mode="lines+markers")
    fig.add_trace(trace)

    channel_std = np.std(channel_data, axis=1)
    channel_95Error = 1.96 * channel_std
    y_upper = (channel_mean + channel_95Error).tolist()
    y_lower = (channel_mean - channel_95Error).tolist()
    trace_95CI = go.Scatter(x=times+times[::-1],
                            y=y_upper+y_lower[::-1],
                            fill="toself",
                            fillcolor="rgba(0,100,80,0.2)",
                            line=dict(color="rgba(255,255,255,0.0)"),
                            hoverinfo="skip",
                            showlegend=False)
    fig.add_trace(trace_95CI)

    fig.update_layout(xaxis_title="Time (msec)", yaxis_title="Voltage")
    fig.show()

    breakpoint()


if __name__ == "__main__":
    main(sys.argv)
