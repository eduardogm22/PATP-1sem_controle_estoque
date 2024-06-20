from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from visualizar import Ui_Visualizar
class visualizar(QDialog):
    def __init__(self,*args,**argvs):
        super(visualizar,self).__init__(*args,**argvs)
        self.ui = Ui_Visualizar()
        self.ui.setupUi(self)

app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    window = visualizar()
    window.show()
sys.exit(app.exec_())