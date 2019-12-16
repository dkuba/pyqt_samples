

from PyQt5.QtWidgets import QMainWindow, QFrame, QGroupBox, QHBoxLayout, QSplitter, \
                            QVBoxLayout, QPushButton, QSpacerItem, QLabel
from PyQt5.Qt import Qt


class MainAppWin(QMainWindow):

    def __init__(self, *args):
        super(QMainWindow, self).__init__(*args)

        #####################################################
        #          Компановка виджетов в главном окне
        #####################################################

        self.resize(1024, 768)
        # главный виджет - рамка, на ней располагаются элементы
        main_frame = QFrame()
        main_frame.setFrameStyle(0)
        main_frame.setFrameShape(QFrame.StyledPanel)
        self.setCentralWidget(main_frame)

        buttons_frame = QFrame()
        buttons_frame.setFixedWidth(150)
        buttons_frame.setFrameStyle(QFrame.StyledPanel)
        button1 = QPushButton('Кнопка')
        button2 = QPushButton('Кнопка2')
        vbox = QVBoxLayout()
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addStretch(1)
        buttons_frame.setLayout(vbox)

        display_area_frame = QFrame()
        display_area_frame.setFrameStyle(QFrame.StyledPanel)
        v_display_layout = QVBoxLayout()
        display_label = QLabel('область отображения данных')
        v_display_layout.addWidget(display_label)
        display_area_frame.setLayout(v_display_layout)

        h_main_layout = QHBoxLayout()
        #h_main_layout.addStretch(0)
        #h_spacer = QSpacerItem()

        h_main_layout.addWidget(buttons_frame)
        h_main_layout.addWidget(display_area_frame)

        main_frame.setLayout(h_main_layout)

