from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys
from visualizar import Ui_Visualizar
from adicionar import Ui_adicionar
class adicionar(QtWidgets.QMainWindow):
    def __init__(self,*args,**argvs):
        super(adicionar,self).__init__(*args,**argvs)
        self.ui = Ui_adicionar()
        self.ui.setupUi(self)
class visualizar(QtWidgets.QMainWindow):
    def __init__(self,*args,**argvs):
        super(visualizar,self).__init__(*args,**argvs)
        self.ui = Ui_Visualizar()
        self.ui.setupUi(self)
        self.ui.btn_add.clicked.connect(self.add)
        
    def add(self):
        self.add_prod = adicionar()
        self.add_prod.show()
            
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = visualizar()
    MainWindow.show()
    sys.exit(app.exec_())

    