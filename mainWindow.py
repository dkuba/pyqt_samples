

from PyQt5.QtWidgets import QMainWindow
from PyQt5.Qt import Qt

import mainWindow_ui


class MainAppWin(QMainWindow):

    def __init__(self, *args):
        super(QMainWindow, self).__init__(*args)

        self.resize(1024, 768)
        mainWindow_ui.setup_ui(self)

    def process_button_clicked_slot(self):
        pass

    def open_data_base_button_clicked_slot(self):
        pass
