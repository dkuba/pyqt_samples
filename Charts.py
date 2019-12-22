import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

import numpy as np


from PyQt5.QtWidgets import QSizePolicy

from mpl_toolkits.mplot3d import Axes3D


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
       # self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        x = np.linspace(0, 1, 5)
        X, Y = np.meshgrid(x, x)

        #Z = np.sin(X*Y)
        Z = (X ** 2 + Y ** 2) / 1e6

        ax = self.figure.add_subplot(projection="3d")
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        print(Z)
        #ax.plot(np.linspace(0, 1, 5), np.linspace(0, 1, 5), [0, 1, 2, 3, 4])

        ax.set_title('PyQt Matplotlib Example')
        self.draw()


if __name__ == '__main__':
   pass