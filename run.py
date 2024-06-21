import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PATP-Grupo-8.visualizar import visualizar

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = visualizar()
    MainWindow.show()
    sys.exit(app.exec_())