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
            medida INTEGER NOT NULL,
            unidade TEXT NOT NULL,
            fornecedor TEXT, 
            fab TEXT, 
            val TEXT)
            """)
        
        # cur.execute("""CREATE TABLE login(
        #     usuario TEXT NOT NULL,
        #     senha TEXT NOT NULL)
        #     """)
        

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
