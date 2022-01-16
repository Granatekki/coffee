import sys
import sqlite3
import csv

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QApplication,
                             QWidget, QDialog)
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.initUI()

    def initUI(self):
        uic.loadUi('main.ui', self)

        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM cofe WHERE id > 0""").fetchall()
        sp = ['id', 'Название сорта', 'Обжарка',
              'Молотый/Цельный', 'Вкус', 'цена', 'Объём']

        #self.tableWidget = QTableWidget(self)
        #self.tableWidget.setGeometry(180, 10, 500, 280)
        self.tableWidget.setColumnCount(len(sp))
        self.tableWidget.setHorizontalHeaderLabels(sp)
        self.tableWidget.setRowCount(len(result))
        for y in range(len(result)):
            self.tableWidget.setItem(y, 0, QTableWidgetItem(str(result[y][0])))
            self.tableWidget.setItem(y, 1, QTableWidgetItem(result[y][1]))
            self.tableWidget.setItem(y, 2, QTableWidgetItem(str(result[y][2])))
            self.tableWidget.setItem(y, 3, QTableWidgetItem(str(result[y][3])))
            self.tableWidget.setItem(y, 4, QTableWidgetItem(str(result[y][4])))
            self.tableWidget.setItem(y, 5, QTableWidgetItem(str(result[y][5])))
            self.tableWidget.setItem(y, 6, QTableWidgetItem(str(result[y][6]))) 
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
