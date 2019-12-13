

from PyQt5.QtWidgets import QMainWindow, QFrame, QGroupBox, QHBoxLayout, QSplitter, \
                            QVBoxLayout
from PyQt5.Qt import Qt


class MainAppWin(QMainWindow):

    def __init__(self, *args):
        super(QMainWindow, self).__init__(*args)

        #####################################################
        #          Компановка виджетов в главном окне
        #####################################################

        self.resize(1024, 768)
        # главный виджет - рамка, на ней располагаются элементы
        mainFrame = QFrame()
        mainFrame.setFrameStyle(0)
        mainFrame.setFrameShape(QFrame.StyledPanel)
        self.setCentralWidget(mainFrame)

        # grpupBox для расположения дерева файлов
        fileTreeBox = QGroupBox()
        fileTreeBox.setContentsMargins(0, 0, 0, 0)

        fileTreeBox.setTitle('Файлы процедур')
        # grpupBox для расположения дерева файлов
        errMsgBox = QGroupBox()
        errMsgBox.setTitle('Окно сообщений')

        hbox = QHBoxLayout()
        splitter1 = QSplitter(Qt.Horizontal)
        #splitter1.addWidget(self.tab)
        # размещаем дерево файлов
        vboxTree = QVBoxLayout()
        vboxTree.setContentsMargins(0, 0, 0, 0)
        #vboxTree.addWidget(self.tree)
        fileTreeBox.setLayout(vboxTree)
        #splitter1.addWidget(fileTreeBox)

        splitter1.setSizes([800, 250])
        splitter1.setStretchFactor(0, 1)
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        # размещаем окно сообщений
        hboxMsg = QHBoxLayout()
        hboxMsg.setContentsMargins(0, 0, 0, 0)
        #hboxMsg.addWidget(self.msg_browser)
        errMsgBox.setLayout(hboxMsg)
        #splitter2.addWidget(errMsgBox)

        splitter2.setSizes([800, 50])
        splitter2.setStretchFactor(0, 1)
        hbox.addWidget(splitter2)
        mainFrame.setLayout(hbox)

