import sqlite3 as lite

con = lite.connect("dados.db")

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE produtos(codigo INTEGER PRIMARY KEY AUTOINCREMENT, desc TEXT, medida TEXT, fornecedor TEXT, fab TEXT, val TEXT)")