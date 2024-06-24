from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog
from
from interface_login import Ui_Login
from query import sqlite_db

class login(QDialog):
    def __init__(self,*args,**argvs):
        super(login,self).__init__(*args,**argvs)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.btn_logar.clicked.connect(self.fazer_login)
        
    def fazer_login(self):
        
    def cadastrar_usuario(self):
        db = sqlite_db("login.db")
        
        user = self.ui.digitar_usuario.text()
        password = self.ui.digitar_senha.text()

        if user == "" or password == "":
            QMessageBox.information(self, "Atenção!", "Preencha os campos obrigatorios!")
        else:
            db.cadastra_apaga_edita("INSERT INTO login(usuario, senha) VALUES('{}', '{}')".format(user, password))
            QMessageBox.information(self, "Cadastro bem sucedido!", "Produto cadastrado com sucesso!")