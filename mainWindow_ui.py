
from PyQt5.QtWidgets import QFrame, QGroupBox, QHBoxLayout, QSplitter, \
                            QVBoxLayout, QPushButton, QSpacerItem, QLabel


def setup_ui(self):
    # кнопки на левой боковой панели
    buttons_frame = QFrame()
    buttons_frame.setFixedWidth(150)
    buttons_frame.setFrameStyle(QFrame.StyledPanel)
    open_data_base_button = QPushButton('Выбрать запись')
    open_data_base_button.clicked.connect(self.open_data_base_button_clicked_clot)
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
    v_display_layout = QVBoxLayout()
    self.display_label = QLabel('область отображения данных')
    v_display_layout.addWidget(self.display_label)
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