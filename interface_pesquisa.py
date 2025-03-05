from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pesquisar(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(701, 259)
        Dialog.setStyleSheet("background-color: rgb(35, 39, 45);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_pesquisar_produto = QtWidgets.QLabel(Dialog)
        self.label_pesquisar_produto.setMinimumSize(QtCore.QSize(291, 51))
        self.label_pesquisar_produto.setMaximumSize(QtCore.QSize(291, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_pesquisar_produto.setFont(font)
        self.label_pesquisar_produto.setStyleSheet("border-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 17pt \"Times New Roman\";")
        self.label_pesquisar_produto.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pesquisar_produto.setObjectName("label_pesquisar_produto")
        self.horizontalLayout.addWidget(self.label_pesquisar_produto)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.digitar_pesquisa = QtWidgets.QLineEdit(Dialog)
        self.digitar_pesquisa.setMinimumSize(QtCore.QSize(0, 25))
        self.digitar_pesquisa.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.digitar_pesquisa.setObjectName("digitar_pesquisa")
        self.verticalLayout.addWidget(self.digitar_pesquisa)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btn_fazer_pesquisa = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_fazer_pesquisa.sizePolicy().hasHeightForWidth())
        self.btn_fazer_pesquisa.setSizePolicy(sizePolicy)
        self.btn_fazer_pesquisa.setMinimumSize(QtCore.QSize(400, 60))
        self.btn_fazer_pesquisa.setMaximumSize(QtCore.QSize(400, 60))
        self.btn_fazer_pesquisa.setStyleSheet("QPushButton{\n"
"    background-color: #2a3137;\n"
"    border-radius: 4px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 14pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover{\n"
"     background-color: #333b42;\n"
"}")
        self.btn_fazer_pesquisa.setObjectName("btn_fazer_pesquisa")
        self.horizontalLayout_2.addWidget(self.btn_fazer_pesquisa)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Pesquisar Produtos"))
        self.label_pesquisar_produto.setText(_translate("Dialog", "Pesquisar Produto"))
        self.btn_fazer_pesquisa.setText(_translate("Dialog", "Pesquisar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Pesquisar()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
