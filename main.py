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
import criar_bd

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
        self.ui.btn_editar.clicked.connect(self.editar)
        self.ui.btn_remove.clicked.connect(self.remover)
        self.ui.btn_pesquisa.clicked.connect(self.presquisar)
           
    def add(self):
        db = criar_bd("dados.db")
        descri = self.ui.digitar_descricao.text()
        med = self.ui.digitar_medida.text()
        fornec = self.ui.digitar_medida.text()
        fabri = self.ui.digitar_fab.text()
        valid = self.ui.digitar_val.text()
        
        db.cadastrar_produtos("INSERT INTO produtos(desc, medida, fornecedor, fab, val) VALUES(?, ?, ?, ?, ?)")
        
        self.add_prod = adicionar()
        self.add_prod.show()
            
    def editar(self):
        pass    
    
    def remover(self):
        pass
        #codigo_id = criar uma tela que peça o numero do id para remover 
      
    def pesquisar(self):
        pass    
    
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = visualizar()
    MainWindow.show()
    sys.exit(app.exec_())

    