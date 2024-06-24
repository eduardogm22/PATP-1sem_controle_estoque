from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys
from interface_visualizar import Ui_Visualizar
from interface_adicionar import Ui_adicionar
from query import sqlite_db
from interface_pesquisa import Ui_Pesquisar
from interface_entrada_saida import Ui_ES

class adicionar(QtWidgets.QMainWindow):
    def __init__(self,mostrar_dados,*args,**argvs):
        super(adicionar,self).__init__(*args,**argvs)
        self.ui = Ui_adicionar()
        self.ui.setupUi(self)
        self.ui.btn_salvar.clicked.connect(self.add)
        self.atualizar = mostrar_dados
        
        quit = QtWidgets.QAction("Quit", self)
        quit.triggered.connect(self.closeEvent)
        
    def closeEvent(self,event):
            self.atualizar()

    def add(self,separar_medida):
        db = sqlite_db("Produtos.db")
        
        descri = self.ui.digitar_descricao.text()
        med = self.ui.digitar_medida.text()
        fornec = self.ui.digitar_fornecedor.text()
        fabri = self.ui.digitar_fab.text()
        valid = self.ui.digitar_val.text()
        
        
        if descri == "" or med == "":
            QMessageBox.information(self, "Atenção!", "Preencha os campos obrigatorios!")
        else:
            medida, unidade = self.separar_medida(med)
            medida = int(medida)
            db.cadastra_apaga_edita("INSERT INTO produtos(desc, medida, unidade, fornecedor, fab, val) VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(descri, medida, unidade, fornec, fabri, valid))
            QMessageBox.information(self, "Cadastro bem sucedido!", "Produto cadastrado com sucesso!")

    def separar_medida(self,med):
        import re
        match = re.match(r"([0-9.]+)\s*([a-zA-Z]*)", med)
        if match:
            numero = match.group(1)
            unidade = match.group(2)
            return float(numero), unidade
        else:
            raise ValueError("Por favor, informe a quantidade e a unidade de medida!")

    
    
class visualizar(QtWidgets.QMainWindow):
    def __init__(self,*args,**argvs):
        super(visualizar,self).__init__(*args,**argvs)
        self.ui = Ui_Visualizar()
        self.ui.setupUi(self)
        self.ui.btn_add.clicked.connect(self.abrir_tela_cadastro)
        self.ui.btn_editar.clicked.connect(self.abrir_es)
        self.ui.btn_remove.clicked.connect(self.remover)
        self.ui.btn_pesquisa.clicked.connect(self.abrir_pesquisar)
        self.mostrar_dados()
        self.ui.treeWidget.itemClicked.connect(self.selecionar_item)
        
    def mostrar_dados(self):
        db = sqlite_db("produtos.db")
        lista = db.recebe_dados("SELECT * FROM produtos")
        
        self.ui.treeWidget.clear()
        for dados in lista:
            produto = QTreeWidgetItem([str(d) for d in dados])
            self.ui.treeWidget.addTopLevelItem(produto)

    def abrir_tela_cadastro(self):
        self.add_window = adicionar(self.mostrar_dados)
        self.add_window.show()
    
    def selecionar_item(self,produto,column):
        produto.setFlags(produto.flags() | QtCore.Qt.ItemIsEditable)
        self.ui.treeWidget.editItem(produto)
            
    
    def remover(self):
        selecionar_item = self.ui.treeWidget.currentItem()
        if selecionar_item:
            id_selecionado = selecionar_item.text(0)
            db = sqlite_db("produtos.db")
            db.cadastra_apaga_edita("DELETE FROM produtos WHERE id = {}".format(id_selecionado))
            
            self.ui.treeWidget.takeTopLevelItem(self.ui.treeWidget.indexOfTopLevelItem(selecionar_item))
      
    def abrir_pesquisar(self):
        pesquisar = Objeto_Pesquisa(self.ui.treeWidget)
        pesquisar.exec_()
        
    def abrir_es(self):
        es = Objeto_ES(self.ui.treeWidget,self.mostrar_dados)
        es.exec_()
class Objeto_Pesquisa(QDialog):
    def __init__(self,treeWidget,*args,**argvs):
        super(Objeto_Pesquisa,self).__init__(*args,**argvs)
        self.ui = Ui_Pesquisar()
        self.ui.setupUi(self)
        self.treeWidget = treeWidget
        self.ui.btn_fazer_pesquisa.clicked.connect(self.procurar_produtos)
        
    def procurar_produtos(self):
        produto_pesquisado = self.ui.digitar_pesquisa.text().lower()
        for i in range(self.treeWidget.topLevelItemCount()):
            produto_cadastrado = self.treeWidget.topLevelItem(i)
            codigo = produto_cadastrado.text(0)
            descricao = produto_cadastrado.text(1).lower()
            if produto_pesquisado in codigo or produto_pesquisado in descricao:
                produto_cadastrado.setHidden(False)
            else:  
                produto_cadastrado.setHidden(True)

class Objeto_ES(QDialog):
    def __init__(self,treeWidget,mostrar_dados,*args,**argvs):
        super(Objeto_ES,self).__init__(*args,**argvs)
        self.ui = Ui_ES()
        self.ui.setupUi(self)
        self.treeWidget = treeWidget
        self.ui.btn_fluxo_salvar.clicked.connect(self.entrada_saida)
        self.atualizar = mostrar_dados
    
    def entrada_saida(self):
        produto_es = self.ui.digitar_id_es.text()
        entrada = self.ui.digitar_entrada.text()
        saida = self.ui.digitar_saida.text()
        if saida:
            saida = int(saida)
            if produto_es and saida != "":
                for i in range(self.treeWidget.topLevelItemCount()):
                    produto_cadastrado = self.treeWidget.topLevelItem(i)
                    codigo = produto_cadastrado.text(0)
                    descricao = produto_cadastrado.text(1).lower()
                    if produto_es == codigo or produto_es == descricao:
                        db = sqlite_db("produtos.db")
                        db.cadastra_apaga_edita("UPDATE produtos SET medida = medida -  ? WHERE id = ?",(saida,codigo))
                        QMessageBox.information(self, "Alteração bem sucedida!", "Saida de produtos registrada!")
                        break
                else: QMessageBox.information(self, "Erro!", "Produto não encontrado!")

        if entrada:
            entrada = int(entrada)
            if produto_es and entrada !="":
                for i in range(self.treeWidget.topLevelItemCount()):
                    produto_cadastrado = self.treeWidget.topLevelItem(i)
                    codigo = produto_cadastrado.text(0)
                    descricao = produto_cadastrado.text(1).lower()
                    if produto_es == codigo or produto_es == descricao:
                        db = sqlite_db("produtos.db")
                        db.cadastra_apaga_edita("UPDATE produtos SET medida = medida +  ? WHERE id = ?",(entrada, codigo))
                        QMessageBox.information(self, "Alteração bem sucedida!", "Entrada de produtos registrada!")
                        break
                else: QMessageBox.information(self, "Erro!", "Produto não encontrado!")
                
        quit = QtWidgets.QAction("Quit", self)
        quit.triggered.connect(self.closeEvent)
        
    def closeEvent(self,event):
            self.atualizar()
            
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = visualizar()
    MainWindow.show()
    sys.exit(app.exec_())

    