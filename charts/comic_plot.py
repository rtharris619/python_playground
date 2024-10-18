import matplotlib.pyplot as plt
import numpy as np


def draw_comic_plot():
    plt.xkcd()

    plt.plot(np.sin(np.linspace(0, 10)))

    plt.title("Comic Plots")
    plt.show()


def driver():
    draw_comic_plot()
