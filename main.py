import sys
import sqlite3
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem, QTableWidget
from random import randrange

class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        con = sqlite3.connect('coffee.db')
        cur = con.cursor()
        result = cur.execute("""Select * from coffee""").fetchall()
        self.tableWidget.setRowCount(len(result))
        for i in range(len(result)):
            for j in range(len(result[0])):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(result[i][j])))
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())