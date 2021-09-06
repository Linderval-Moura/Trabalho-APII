import sqlite3 as sql 

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

def login(nome="", senha=""):
    trans = Transicao()
    trans.connect()
    trans.execute("SELECT nome, senha FROM clientes")
    rows = trans.fetchall()
    if (nome, senha) in rows:
        print("Ok")
        
        #exec(open(pastaroot+"\\Doador_P.py").read())

    else :
        print((nome, senha))
    trans.disconnect()
    return rows