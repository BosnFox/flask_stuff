import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.draw_)

    def draw_(self):
        self.draw = DrawWinget()
        self.draw.show()
        self.close()


class DrawWinget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.do_paint = False
        self.pressed_b = 3
        self.p_x = 0
        self.p_y = 0
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Formes par coordonnées')

    def mousePressEvent(self, event):
        self.p_y = int(event.y())
        self.p_x = int(event.x())
        if event.button() == Qt.LeftButton:
            self.pressed_b = 1
        else:
            self.pressed_b = 2
        self.paint()

    def mouseMoveEvent(self, event):
        self.p_x = int(event.x())
        self.p_y = int(event.y())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.pressed_b = 3
        self.paint()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_(qp)
            qp.end()

    def draw_(self, qp):
        qp.setBrush(QColor('Yellow'))
        s = randint(1, 100)
        if self.pressed_b:
            qp.drawEllipse(self.p_x - s, self.p_y - s, s * 2, s * 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
