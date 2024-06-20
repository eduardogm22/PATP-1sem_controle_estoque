
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Visualizar(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1226, 777)
        MainWindow.setStyleSheet("background-color: rgb(35, 39, 45);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.janelas_principais = QtWidgets.QStackedWidget(self.centralwidget)
        self.janelas_principais.setObjectName("janelas_principais")
        self.page_produtos = QtWidgets.QWidget()
        self.page_produtos.setObjectName("page_produtos")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_produtos)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_pesquisa = QtWidgets.QPushButton(self.page_produtos)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pesquisa.sizePolicy().hasHeightForWidth())
        self.btn_pesquisa.setSizePolicy(sizePolicy)
        self.btn_pesquisa.setMinimumSize(QtCore.QSize(90, 60))
        self.btn_pesquisa.setMaximumSize(QtCore.QSize(120, 60))
        self.btn_pesquisa.setStyleSheet("QPushButton{\n"
"    background-color: #2a3137;\n"
"    border-radius: 4px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover{\n"
"     background-color: #333b42;\n"
"}")
        self.btn_pesquisa.setObjectName("btn_pesquisa")
        self.horizontalLayout.addWidget(self.btn_pesquisa)
        self.btn_add = QtWidgets.QPushButton(self.page_produtos)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy)
        self.btn_add.setMinimumSize(QtCore.QSize(90, 60))
        self.btn_add.setMaximumSize(QtCore.QSize(120, 60))
        self.btn_add.setStyleSheet("QPushButton{\n"
"    background-color: #2a3137;\n"
"    border-radius: 4px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover{\n"
"     background-color: #333b42;\n"
"}")
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout.addWidget(self.btn_add)
        self.btn_remove = QtWidgets.QPushButton(self.page_produtos)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_remove.sizePolicy().hasHeightForWidth())
        self.btn_remove.setSizePolicy(sizePolicy)
        self.btn_remove.setMinimumSize(QtCore.QSize(90, 60))
        self.btn_remove.setMaximumSize(QtCore.QSize(120, 60))
        self.btn_remove.setStyleSheet("QPushButton{\n"
"    background-color: #2a3137;\n"
"    border-radius: 4px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover{\n"
"     background-color: #333b42;\n"
"}")
        self.btn_remove.setObjectName("btn_remove")
        self.horizontalLayout.addWidget(self.btn_remove)
        self.btn_editar = QtWidgets.QPushButton(self.page_produtos)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_editar.sizePolicy().hasHeightForWidth())
        self.btn_editar.setSizePolicy(sizePolicy)
        self.btn_editar.setMinimumSize(QtCore.QSize(90, 60))
        self.btn_editar.setMaximumSize(QtCore.QSize(120, 60))
        self.btn_editar.setStyleSheet("QPushButton{\n"
"    background-color: #2a3137;\n"
"    border-radius: 4px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover{\n"
"     background-color: #333b42;\n"
"}")
        self.btn_editar.setObjectName("btn_editar")
        self.horizontalLayout.addWidget(self.btn_editar)
        self.label_titulo = QtWidgets.QLabel(self.page_produtos)
        self.label_titulo.setStyleSheet("background-color: #2a3137;\n"
"border-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 40pt \"Times New Roman\";")
        self.label_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titulo.setObjectName("label_titulo")
        self.horizontalLayout.addWidget(self.label_titulo)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.treeWidget = QtWidgets.QTreeWidget(self.page_produtos)
        self.treeWidget.setStyleSheet("")
        self.treeWidget.setObjectName("treeWidget")
        self.verticalLayout_3.addWidget(self.treeWidget)
        self.janelas_principais.addWidget(self.page_produtos)
        self.page_cadastro = QtWidgets.QWidget()
        self.page_cadastro.setObjectName("page_cadastro")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_cadastro)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_cadastro_prod = QtWidgets.QLabel(self.page_cadastro)
        self.label_cadastro_prod.setMaximumSize(QtCore.QSize(1500, 70))
        self.label_cadastro_prod.setStyleSheet("border-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 30pt \"Times New Roman\";")
        self.label_cadastro_prod.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cadastro_prod.setObjectName("label_cadastro_prod")
        self.verticalLayout_2.addWidget(self.label_cadastro_prod)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_descricao = QtWidgets.QLabel(self.page_cadastro)
        self.label_descricao.setMinimumSize(QtCore.QSize(110, 25))
        self.label_descricao.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_descricao.setFont(font)
        self.label_descricao.setStyleSheet("border-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 17pt \"Times New Roman\";")
        self.label_descricao.setAlignment(QtCore.Qt.AlignCenter)
        self.label_descricao.setObjectName("label_descricao")
        self.horizontalLayout_2.addWidget(self.label_descricao)
        self.digitar_descricao = QtWidgets.QLineEdit(self.page_cadastro)
        self.digitar_descricao.setMinimumSize(QtCore.QSize(0, 25))
        self.digitar_descricao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.digitar_descricao.setObjectName("digitar_descricao")
        self.horizontalLayout_2.addWidget(self.digitar_descricao)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_medida = QtWidgets.QLabel(self.page_cadastro)
        self.label_medida.setMinimumSize(QtCore.QSize(110, 0))
        self.label_medida.setMaximumSize(QtCore.QSize(100, 25))
        self.label_medida.setStyleSheet("border-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 17pt \"Times New Roman\";")
        self.label_medida.setAlignment(QtCore.Qt.AlignCenter)
        self.label_medida.setObjectName("label_medida")
        self.horizontalLayout_7.addWidget(self.label_medida)
        self.digitar_medida = QtWidgets.QLineEdit(self.page_cadastro)
        self.digitar_medida.setMinimumSize(QtCore.QSize(0, 25))
        self.digitar_medida.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.digitar_medida.setObjectName("digitar_medida")
        self.horizontalLayout_7.addWidget(self.digitar_medida)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_fornecedor = QtWidgets.QLabel(self.page_cadastro)
        self.label_fornecedor.setMinimumSize(QtCore.QSize(110, 0))
        self.label_fornecedor.setMaximumSize(QtCore.QSize(100, 25))
        self.label_fornecedor.setStyleSheet("border-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 17pt \"Times New Roman\";")
        self.label_fornecedor.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fornecedor.setObjectName("label_fornecedor")
        self.horizontalLayout_8.addWidget(self.label_fornecedor)
        self.digitar_fornecedor = QtWidgets.QLineEdit(self.page_cadastro)
        self.digitar_fornecedor.setMinimumSize(QtCore.QSize(0, 25))
        self.digitar_fornecedor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.digitar_fornecedor.setObjectName("digitar_fornecedor")
        self.horizontalLayout_8.addWidget(self.digitar_fornecedor)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_fab = QtWidgets.QLabel(self.page_cadastro)
        self.label_fab.setMinimumSize(QtCore.QSize(110, 0))
        self.label_fab.setMaximumSize(QtCore.QSize(100, 25))
        self.label_fab.setStyleSheet("border-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 17pt \"Times New Roman\";")
        self.label_fab.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fab.setObjectName("label_fab")
        self.horizontalLayout_6.addWidget(self.label_fab)
        self.digitar_fab = QtWidgets.QLineEdit(self.page_cadastro)
        self.digitar_fab.setMinimumSize(QtCore.QSize(0, 25))
        self.digitar_fab.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.digitar_fab.setObjectName("digitar_fab")
        self.horizontalLayout_6.addWidget(self.digitar_fab)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_val = QtWidgets.QLabel(self.page_cadastro)
        self.label_val.setMinimumSize(QtCore.QSize(110, 0))
        self.label_val.setMaximumSize(QtCore.QSize(100, 25))
        self.label_val.setStyleSheet("border-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 17pt \"Times New Roman\";")
        self.label_val.setAlignment(QtCore.Qt.AlignCenter)
        self.label_val.setObjectName("label_val")
        self.horizontalLayout_5.addWidget(self.label_val)
        self.digitar_val = QtWidgets.QLineEdit(self.page_cadastro)
        self.digitar_val.setMinimumSize(QtCore.QSize(0, 25))
        self.digitar_val.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.digitar_val.setObjectName("digitar_val")
        self.horizontalLayout_5.addWidget(self.digitar_val)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_salvar = QtWidgets.QPushButton(self.page_cadastro)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_salvar.sizePolicy().hasHeightForWidth())
        self.btn_salvar.setSizePolicy(sizePolicy)
        self.btn_salvar.setMinimumSize(QtCore.QSize(90, 60))
        self.btn_salvar.setMaximumSize(QtCore.QSize(400, 60))
        self.btn_salvar.setStyleSheet("QPushButton{\n"
"    background-color: #2a3137;\n"
"    border-radius: 4px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover{\n"
"     background-color: #333b42;\n"
"}")
        self.btn_salvar.setObjectName("btn_salvar")
        self.horizontalLayout_3.addWidget(self.btn_salvar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.janelas_principais.addWidget(self.page_cadastro)
        self.verticalLayout.addWidget(self.janelas_principais)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.janelas_principais.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_pesquisa.setText(_translate("MainWindow", "Pesquisar"))
        self.btn_add.setText(_translate("MainWindow", "Adicionar"))
        self.btn_remove.setText(_translate("MainWindow", "Remover"))
        self.btn_editar.setText(_translate("MainWindow", "Editar"))
        self.label_titulo.setText(_translate("MainWindow", "Estoque Ideau"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Código"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Descrição"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Medida"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Fornecedor"))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "Fabricação"))
        self.treeWidget.headerItem().setText(5, _translate("MainWindow", "Validade"))
        self.label_cadastro_prod.setText(_translate("MainWindow", "Cadastro de Produtos"))
        self.label_descricao.setText(_translate("MainWindow", "Descrição"))
        self.label_medida.setText(_translate("MainWindow", "Medida"))
        self.label_fornecedor.setText(_translate("MainWindow", "Fornecedor"))
        self.label_fab.setText(_translate("MainWindow", "Fabricação"))
        self.label_val.setText(_translate("MainWindow", "Validade"))
        self.btn_salvar.setText(_translate("MainWindow", "Adicionar"))

import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Visualizar()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


