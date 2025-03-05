from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QMainWindow
from PyQt5 import QtWidgets
from interface_login import Ui_Login
from interface_visualizar import Ui_Visualizar
import sys

class Objeto_Login(QDialog):
    def __init__(self, *args, **kwargs):
        super(Objeto_Login, self).__init__(*args, **kwargs)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.btn_logar.clicked.connect(self.fazer_login)
        
    def fazer_login(self):
        user = self.ui.digitar_usuario.text()
        password = self.ui.digitar_senha.text()
        usuario = "admin"
        senha = "admin"
        
        if user == usuario and senha == password:
            self.abrir_visualizar()
        else:
            QMessageBox.warning(self, "Não foi possível logar!", "Usuário e/ou senha incorretos")
    
    def abrir_visualizar(self):
        # Criar uma QMainWindow temporária para exibir a interface Ui_Visualizar
        self.visualizar_window = QMainWindow()
        self.ui_visualizar = Ui_Visualizar()
        self.ui_visualizar.setupUi(self.visualizar_window)
        self.visualizar_window.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginn = QtWidgets.QMainWindow()
    ui = Objeto_Login()
    ui.setupUi(loginn)
    loginn.show()
    sys.exit(app.exec_())
