
import sys
from PyQt5.QtWidgets import QApplication, QStyleFactory

from mainWindow import *


if __name__ == '__main__':

    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    # app.setStyleSheet(str(qssStr))
    myGUI = MainAppWin()
    myGUI.show()
    sys.exit(app.exec_())
