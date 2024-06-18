from PyQt5 import uic, QtCore, QtGui, QtWidgets

app=QtWidgets.QApplication([])
tela_visualizar=uic.loadUi("interface_pg_visu.py")

tela_visualizar.show()
app.exec()