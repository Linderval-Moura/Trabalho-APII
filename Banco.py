import sqlite3 as sql 
import os

# Metodos da barra de menu 
pastaroot = os.path.dirname(__file__)

# C - Create     |    criando o banco
# R - Read       |    E o Login
# U - Update     | 
# D - Delete     |

# conectando o ‘clientes.db’,
# cria a tabela cliente se não existir
class Transicao():
    database    = "clientes.db"
    conn        = None
    cur         = None
    connected   = False

    def connect(self): # conexão com o banco
        Transicao.conn      = sql.connect(Transicao.database)
        Transicao.cur       = Transicao.conn.cursor()
        Transicao.connected = True

    def disconnect(self): # fecha conexão
        Transicao.conn.close()
        Transicao.connected = False

    def execute(self, sql, parms = None): # 
        if Transicao.connected:
            if parms == None:
                Transicao.cur.execute(sql)
            else:
                Transicao.cur.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self):
        return Transicao.cur.fetchall()

    def persist(self):
        if Transicao.connected:
            Transicao.conn.commit()
            return True
        else:
            return False



def initDB():
    trans = Transicao()
    trans.connect()
    trans.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY , nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT,telefone TEXT,senha TEXT)")
    trans.persist()
    trans.disconnect()

def insert(nome, sobrenome, email, cpf, telefone, senha):
    trans = Transicao()
    trans.connect()
    trans.execute("INSERT INTO clientes VALUES(NULL, ?,?,?,?,?,?)", (nome, sobrenome, email, cpf, telefone, senha))
    trans.persist()
    trans.disconnect()


def view(nome, sobrenome, email, cpf, telefone):
    trans = Transicao()
    trans.connect()
    trans.execute("SELECT id, nome, sobrenome, email, cpf, telefone FROM clientes")
    rows = trans.fetchall()
    trans.disconnect()
    return rows
#insert  search
def search(nome="", sobrenome="", email="", cpf="", telefone="" ,senha=""):
    trans = Transicao()
    trans.connect()
    trans.execute("SELECT * FROM clientes WHERE nome=? or sobrenome=? or email=? or cpf=? or telefone=? or senha=?", (nome,sobrenome,email, cpf, telefone, senha))
    rows = trans.fetchall()
    trans.disconnect()
    return rows


def delete(id):
    trans = Transicao()
    trans.connect()
    trans.execute("DELETE FROM clientes WHERE id = ?", (id,))
    trans.persist()
    trans.disconnect()

def update(id, nome, sobrenome, email, cpf, telefone, senha):
    trans = Transicao()
    trans.connect()
    trans.execute("UPDATE clientes SET nome =?, sobrenome=?, email=?, cpf=?, telefone=?, senha=? WHERE id = ?",(nome, sobrenome,email, cpf, telefone, senha, id))
    trans.persist()
    trans.disconnect()

def login(nome="", senha=""):
    trans = Transicao()
    trans.connect()
    trans.execute("SELECT nome, senha FROM clientes")
    rows = trans.fetchall()
    if (nome, senha) in rows:
        print("Ok")
        
        #exec(open(pastaroot+"\\Login.py").read())

    else :
        print("ERRO! Voce digitou:")
        print((nome, senha))
    trans.disconnect()
    return rows



initDB()


