import sqlite3 as lite

con = lite.connect("dados.db")

"""dados = ["Seringa", "5ML", "Descarpack", "10/08/2023", "Indefinido"]

#cadastrar produtos
with con:
    cur = con.cursor()
    query = "INSERT INTO produtos(desc, medida, fornecedor, fab, val) VALUES(?, ?, ?, ?, ?)"
    cur.execute(query, dados)

#crud


atualizar_dados = ["Becker", "5ML", "Descarpack", "10/08/2023", "Indefinido", 1 ]
#atualizar produtos
with con:
    cur = con.cursor()
    query = "UPDATE produtos SET desc=?, medida=?, fornecedor=?, fab=?, val=? WHERE id=? "
    cur.execute(query,atualizar_dados)"""
    
deletar_dados = str(4)  
#remover produtos
with con:
    cur = con.cursor()
    query = "DELETE FROM produtos WHERE id=?"
    cur.execute(query,deletar_dados)

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