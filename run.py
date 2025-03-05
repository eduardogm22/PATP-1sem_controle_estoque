import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PATP-Grupo-8.interface_visualizar import interface_visualizar

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = interface_visualizar()
    MainWindow.show()
    sys.exit(app.exec_())