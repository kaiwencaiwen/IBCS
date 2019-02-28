import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt


class MyWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__()
		uic.loadUi('demo.ui', self)
		self.addtable.clicked.connect(self.f_addtable)
		self.revtable.clicked.connect(self.f_revtable)
		self.addrow.clicked.connect(self.f_addrow)
		self.revrow.clicked.connect(self.f_revrow)
		self.addcol.clicked.connect(self.f_addcol)
		self.revcol.clicked.connect(self.f_revcol)
		self.show()

	def f_addtable(self):
		print("table added")
		self.tableWidget.setRowCount(4)
		self.tableWidget.setColumnCount(2)
		self.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem("Cell (1,1)"))
		self.tableWidget.setItem(0,1, QtWidgets.QTableWidgetItem("Cell (1,2)"))
		self.tableWidget.setItem(1,0, QtWidgets.QTableWidgetItem("Cell (2,1)"))
		self.tableWidget.setItem(1,1, QtWidgets.QTableWidgetItem("Cell (2,2)"))
		self.tableWidget.setItem(2,0, QtWidgets.QTableWidgetItem("Cell (3,1)"))
		self.tableWidget.setItem(2,1, QtWidgets.QTableWidgetItem("Cell (3,2)"))
		self.tableWidget.setItem(3,0, QtWidgets.QTableWidgetItem("Cell (4,1)"))
		self.tableWidget.setItem(3,1, QtWidgets.QTableWidgetItem("Cell (4,2)"))
		self.show()

	def f_revtable(self):
		print("table removed")

	def f_addrow(self):
		print("row added")

	def f_revrow(self):
		print("row removed")

	def f_addcol(self):
		print("column added")

	def f_revcol(self):
		print("column removed")
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = MyWindow()

	sys.exit(app.exec_())
