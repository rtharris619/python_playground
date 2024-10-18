import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


class AnimatedScatterPlot:

    def __init__(self):
        pass

    def draw_animated_scatter_plot(self):

        self.num_points = 100

        self.x, self.y = np.random.rand(2, self.num_points) * 10
        colors = np.random.rand(self.num_points)
        sizes = np.random.rand(self.num_points) * 1000

        self.fig, ax = plt.subplots()
        self.scat = ax.scatter(self.x, self.y, c=colors, s=sizes)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

    def animate(self, i):
        self.scat.set_offsets(np.c_[self.x + np.random.randn(self.num_points) * 0.1, self.y + np.random.randn(self.num_points) * 0.1])

    def plot(self):
        self.draw_animated_scatter_plot()
        ani = animation.FuncAnimation(self.fig, self.animate, frames=100, interval=50)
        plt.show()


def driver():
    asp = AnimatedScatterPlot()
    asp.plot()
