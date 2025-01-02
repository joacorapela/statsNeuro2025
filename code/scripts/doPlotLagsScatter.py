
import sys
import argparse
import numpy as np
import scipy.io
import plotly.graph_objects as go


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--trial_index", type=int, help="trial index",
                        default=0)
    parser.add_argument("--channel_label", type=str, help="channels label",
                        default="Cz")
    parser.add_argument("--lag_sec", type=float, help="lag (sec)",
                        default=0.062)
    parser.add_argument("--data_filename", type=str, help="data filename",
                        default="../../../data/D_01_cleaned.mat")
    args = parser.parse_args()

    trial_index = args.trial_index
    channel_label = args.channel_label
    lag_sec = args.lag_sec
    data_filename = args.data_filename

    mat = scipy.io.loadmat(data_filename)
    data = mat["data"]
    srate = mat["srate"]
    # times = mat["times"]
    n_channels = len(mat["chanlabels"][0])

    lag_samples = int(lag_sec * srate)

    # get channel labels
    chanlabels = [None] * n_channels
    for i in range(n_channels):
        chanlabels[i] = mat["chanlabels"][0][i][0]

    channel_index = chanlabels.index(channel_label)

    fig = go.Figure()
    channel_data = data[channel_index, :, trial_index]
    x = channel_data[lag_samples:]
    y = channel_data[:-lag_samples]
    mu_hat = channel_data.mean()
    var_hat = channel_data.var()
    cor = np.mean((x-mu_hat) * (y-mu_hat))/var_hat
    trace = go.Scatter(x=x, y=y, mode="markers")
    fig.add_trace(trace)
    fig.update_layout(title=f"cor={cor:.2f}",
                      xaxis_title=f"lag(x, {lag_sec} sec)",
                      yaxis_title="x")
    fig.show()

    breakpoint()


if __name__ == "__main__":
    main(sys.argv)
