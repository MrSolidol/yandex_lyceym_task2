import sys, random
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.kek = []
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton_2.clicked.connect(self.run)
    def run(self):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.kek.append((random.randint(-50, 400), random.randint(0, 400),
                         random.randint(5, 200), color))
        self.update()

    def paintEvent(self, event):
        self.painter = QPainter()
        self.painter.begin(self)
        for i in self.kek:
            self.painter.setBrush(QColor(*i[3]))
            self.painter.drawEllipse(i[0], i[1], i[2], i[2])
        self.painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())