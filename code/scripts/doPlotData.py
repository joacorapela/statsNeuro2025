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
    times = mat["times"].flatten()
    n_channels = len(mat["chanlabels"][0])

    # get channel labels
    chanlabels = [None] * n_channels
    for i in range(n_channels):
        chanlabels[i] = mat["chanlabels"][0][i][0]

    channel_index = chanlabels.index(channel_label)


    n_trials = data.shape[2]
    fig = go.Figure()
    for r in range(n_trials):
        channel_data = data[channel_index, :, r]
        trace = go.Scatter(x=times, y=channel_data, mode="lines+markers",
                           name=f"trial {r}")
        fig.add_trace(trace)
    fig.update_layout(xaxis_title="Time (msec)", yaxis_title="Voltage")
    fig.show()

    breakpoint()


if __name__ == "__main__":
    main(sys.argv)
