from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(701, 542)
        MainWindow.setStyleSheet("background-color: rgb(35, 39, 45);")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        
        self.label_login = QtWidgets.QLabel(self.centralwidget)
        self.label_login.setMinimumSize(QtCore.QSize(291, 51))
        self.label_login.setMaximumSize(QtCore.QSize(291, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_login.setFont(font)
        self.label_login.setStyleSheet("border-radius: 0px;\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "font: 75 17pt \"Times New Roman\";")
        self.label_login.setAlignment(QtCore.Qt.AlignCenter)
        self.label_login.setObjectName("label_login")
        self.horizontalLayout_4.addWidget(self.label_login)
        
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        
        spacerItem2 = QtWidgets.QSpacerItem(20, 52, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        self.label_usuario = QtWidgets.QLabel(self.centralwidget)
        self.label_usuario.setMinimumSize(QtCore.QSize(120, 30))
        self.label_usuario.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_usuario.setFont(font)
        self.label_usuario.setStyleSheet("border-radius: 0px;\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "font: 75 17pt \"Times New Roman\";")
        self.label_usuario.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_usuario.setObjectName("label_usuario")
        self.horizontalLayout_3.addWidget(self.label_usuario)
        
        self.digitar_usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.digitar_usuario.setMinimumSize(QtCore.QSize(520, 30))
        self.digitar_usuario.setMaximumSize(QtCore.QSize(1000, 1000))
        self.digitar_usuario.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.digitar_usuario.setObjectName("digitar_usuario")
        self.horizontalLayout_3.addWidget(self.digitar_usuario)
        
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        
        spacerItem3 = QtWidgets.QSpacerItem(20, 52, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.label_senha = QtWidgets.QLabel(self.centralwidget)
        self.label_senha.setMinimumSize(QtCore.QSize(120, 30))
        self.label_senha.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_senha.setFont(font)
        self.label_senha.setStyleSheet("border-radius: 0px;\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "font: 75 17pt \"Times New Roman\";")
        self.label_senha.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_senha.setObjectName("label_senha")
        self.horizontalLayout_2.addWidget(self.label_senha)
        
        self.digitar_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.digitar_senha.setMinimumSize(QtCore.QSize(520, 30))
        self.digitar_senha.setMaximumSize(QtCore.QSize(1000, 1000))
        self.digitar_senha.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.digitar_senha.setObjectName("digitar_senha")
        self.horizontalLayout_2.addWidget(self.digitar_senha)
        
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        
        spacerItem4 = QtWidgets.QSpacerItem(20, 52, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        
        self.btn_logar = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_logar.sizePolicy().hasHeightForWidth())
        self.btn_logar.setSizePolicy(sizePolicy)
        self.btn_logar.setMinimumSize(QtCore.QSize(400, 60))
        self.btn_logar.setMaximumSize(QtCore.QSize(400, 60))
        self.btn_logar.setStyleSheet("QPushButton{\n"
                                      "    background-color: #2a3137;\n"
                                      "    border-radius: 4px;\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    font: 75 14pt \"Segoe UI\";\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "     background-color: #333b42;\n"
                                      "}")
        self.btn_logar.setObjectName("btn_logar")
        self.horizontalLayout.addWidget(self.btn_logar)
        
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        spacerItem7 = QtWidgets.QSpacerItem(20, 24, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label_login.setText(_translate("MainWindow", "Login"))
        self.label_usuario.setText(_translate("MainWindow", "Usuário"))
        self.digitar_usuario.setPlaceholderText(_translate("MainWindow", "Digite o usuário"))
        self.label_senha.setText(_translate("MainWindow", "Senha"))
        self.digitar_senha.setPlaceholderText(_translate("MainWindow", "Digite a senha"))
        self.btn_logar.setText(_translate("MainWindow", "Salvar"))

