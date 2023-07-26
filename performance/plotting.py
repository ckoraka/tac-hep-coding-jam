from __future__ import annotations

import matplotlib.pyplot as plt


# Takes an array of outputs from the timing function, a corresponding label array for the legend and a plot name
def plotting(timing_arr, label_arr, fig_name):
    # fig = plt.figure()
    for timing, label in zip(timing_arr, label_arr):  # Add each set of data to plot
        plt.errorbar(
            timing[:, 0],
            timing[:, 1],
            yerr=timing[:, 2],
            marker="o",
            linestyle="None",
            label=label,
        )

    plt.xlabel("Matrix size (n)")
    plt.ylabel("Time (s)")
    plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 5))
    plt.legend(loc="lower right")
    plt.savefig(fig_name)
