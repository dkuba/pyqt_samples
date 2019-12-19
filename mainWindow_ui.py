
from PyQt5.QtWidgets import QFrame, QGroupBox, QHBoxLayout, QSplitter, \
                            QVBoxLayout, QPushButton, QSpacerItem, QLabel

from PyQt5 import QtCore

from pyqtgraph import PlotWidget, plot
import pyqtgraph.opengl as gl

import pyqtgraph as pg


def setup_ui(self):
    # кнопки на левой боковой панели
    buttons_frame = QFrame()
    buttons_frame.setFixedWidth(150)
    buttons_frame.setFrameStyle(QFrame.StyledPanel)
    open_data_base_button = QPushButton('Выбрать запись')
    open_data_base_button.clicked.connect(self.open_data_base_button_clicked_slot)
    process_button = QPushButton('Отобразить')
    process_button.setEnabled(False)
    process_button.clicked.connect(self.process_button_clicked_slot)
    vbox = QVBoxLayout()

    vbox.addWidget(open_data_base_button)
    vbox.addWidget(process_button)
    vbox.addStretch(1)
    buttons_frame.setLayout(vbox)

    # область отображения данных
    # здесь будет располагаться таблица и график
    display_area_frame = QFrame()
    display_area_frame.setFrameStyle(QFrame.StyledPanel)
    # график
    graph_view = gl.GLViewWidget()

    # create three grids, add each to the view
    xgrid = gl.GLGridItem()
    ygrid = gl.GLGridItem()
    zgrid = gl.GLGridItem()
    graph_view.addItem(xgrid)
    graph_view.addItem(ygrid)
    graph_view.addItem(zgrid)

    # rotate x and y grids to face the correct direction
    xgrid.rotate(90, 0, 1, 0)
    ygrid.rotate(90, 1, 0, 0)

    # scale each grid differently
    xgrid.scale(0.2, 0.1, 0.1)
    ygrid.scale(0.2, 0.1, 0.1)
    zgrid.scale(0.1, 0.2, 0.1)

    # рамка таблицы
    table_frame = QFrame()
    table_frame.setFrameStyle(0)
    table_frame.setFrameShape(QFrame.StyledPanel)

    v_display_layout = QVBoxLayout()
    v_display_layout.addWidget(graph_view)
    v_display_layout.addWidget(table_frame)
    display_area_frame.setLayout(v_display_layout)

    # главный виджет - рамка, на ней располагаются элементы
    main_frame = QFrame()
    main_frame.setFrameStyle(0)
    main_frame.setFrameShape(QFrame.StyledPanel)
    self.setCentralWidget(main_frame)
    h_main_layout = QHBoxLayout()
    h_main_layout.addWidget(buttons_frame)
    h_main_layout.addWidget(display_area_frame)


    main_frame.setLayout(h_main_layout)