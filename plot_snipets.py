import plotly.offline as po
import plotly.graph_objects as go

import pandas as pd

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore, QtWidgets
import sys


def show_qt(fig):
    raw_html = '<html><head><meta charset="utf-8" />'
    raw_html += '<script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head>'
    raw_html += '<body>'
    raw_html += po.plot(fig, include_plotlyjs=False, output_type='div')
    raw_html += '</body></html>'

    fig_view = QWebEngineView()
    # setHtml has a 2MB size limit, need to switch to setUrl on tmp file
    # for large figures.
    fig_view.setHtml(raw_html)
    fig_view.show()
    fig_view.raise_()
    return fig_view


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    # Read data from a csv
    z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
    print(z_data.columns)

    fig = go.Figure(data=[go.Surface(z=z_data.values)])

    fig.update_layout(title='Mt Bruno Elevation', autosize=False,
                      width=500, height=500,
                      margin=dict(l=65, r=50, b=65, t=90))

    fig_view = show_qt(fig)
    sys.exit(app.exec_())
# # library
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns
#
# # Get the data (csv file is hosted on the web)
# url = 'https://python-graph-gallery.com/wp-content/uploads/volcano.csv'
# data = pd.read_csv(url)
#
# # Transform it to a long format
# df = data.unstack().reset_index()
# df.columns = ["X", "Y", "Z"]
#
# # And transform the old column name in something numeric
# df['X'] = pd.Categorical(df['X'])
# df['X'] = df['X'].cat.codes
#
# # Make the plot
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.viridis, linewidth=0.2)
# plt.show()
#
# # # to Add a color bar which maps values to colors.
# # surf = ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.viridis, linewidth=0.2)
# # fig.colorbar(surf, shrink=0.5, aspect=5)
# # plt.show()
# #
# # # Rotate it
# # ax.view_init(30, 45)
# # plt.show()
# #
# # # Other palette
# # ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.jet, linewidth=0.01)
# # plt.show()
