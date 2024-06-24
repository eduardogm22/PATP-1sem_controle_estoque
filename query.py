import sqlite3

class sqlite_db:
    def __init__(self,banco=None):
        self.conn = None
        self.cursor = None
        
        if banco:
            self.open(banco)

    def open(self,banco):
        try:
            self.conn = sqlite3.connect(banco)
            self.cursor = self.conn.cursor()
            print("Conexão estabelecida")
        except sqlite3.Error as e:
            print("Conexão falhou!")
    
    def criar_tabela(self):
        cur = self.cursor
        cur.execute("""CREATE TABLE produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            desc TEXT NOT NULL, 
            medida TEXT NOT NULL, 
            fornecedor TEXT, 
            fab TEXT, 
            val TEXT)
            """)

    def cadastra_apaga_edita(self,query,pesquisa=()):
        try:
            cur = self.cursor
            cur.execute(query,pesquisa)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao executar a query: {e}")

            
    def recebe_dados(self,query):
        cur = self.cursor
        cur.execute(query)
        return cur.fetchall()

db = sqlite_db("Produtos.db")

#db.criar_tabela()






"""con = lite.connect("dados.db")

#cadastrar produtos
def cadastrar_produtos(self,query):
    with con:
        cur = con.cursor()
        query = "INSERT INTO produtos(desc, medida, fornecedor, fab, val) VALUES(?, ?, ?, ?, ?)"
        cur.execute(query)

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

#editar, apagar e atualizar
def edita_apaga_atualiza(self,query):
    cur = self.cursor
    

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
"""