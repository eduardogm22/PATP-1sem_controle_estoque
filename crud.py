import sqlite3 as lite

con = lite.connect("dados.db")

"""dados = ["Seringa", "5ML", "Descarpack", "10/08/2023", "Indefinido"]

#cadastrar produtos
with con:
    cur = con.cursor()
    query = "INSERT INTO produtos(desc, medida, fornecedor, fab, val) VALUES(?, ?, ?, ?, ?)"
    cur.execute(query, dados)
"""
ver_dados = []

#visualizar produtos
with con:
    cur = con.cursor()
    query = "SELECT * FROM produtos"
    cur.execute(query)
    
    rows = cur.fetchall()
    for row in rows:
        ver_dados.append(row)
        
print(ver_dados)