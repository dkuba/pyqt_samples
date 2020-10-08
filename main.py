
import sys
from PyQt5.QtWidgets import QApplication, QStyleFactory
from mainWindow import *


if __name__ == '__main__':

    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    #comment from forker 3
    myGUI = MainAppWin()
    myGUI.show()
    sys.exit(app.exec_())
