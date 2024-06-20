import sqlite3 as lite

con = lite.connect("dados.db")

#cadastrar produtos
def cadastrar_produtos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO produtos(desc, medida, fornecedor, fab, val) VALUES(?, ?, ?, ?, ?)"
        cur.execute(query,i)

#visualizar produtos
def visualizar_produtos():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM produtos"
        cur.execute(query)
        
        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados
        
#pesquisar produtos
def pesquisa_produtos(id):
    pesquisa_pdt = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM produtos WHERE id=?",
        cur.execute(query,id)
        
        rows = cur.fetchall()
        for row in rows:
            pesquisa_pdt.append(row)

#atualizar produtos
def atualizar_produtos(i):
    with con:
        cur = con.cursor()
        query = "UPDATE produtos SET desc=?, medida=?, fornecedor=?, fab=?, val=? WHERE id=? "
        cur.execute(query,i)
    
#remover produtos
def remover_produtos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM produtos WHERE id=?"
        cur.execute(query,i)
