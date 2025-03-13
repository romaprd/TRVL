import sqlite3

def conectar_banco():
    conexao = sqlite3.connect("trvl.db")
    return conexao 

def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''create table if not exists usuarios
                   (email text primary key,nome text,senha text)''')
    
    cursor.execute('''create table if not exists projetos_de_viagem
                   (id integer primary key,id_usuario text,destino text,data_prevista text,
                   status text,imagem text,gastos real,dinheiro_guardado real)''')
    
    conexao.commit()

def criar_usuario(email, nome, senha):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        # PREENCHA AQUI - QUAL O COMANDO CRIAR UM NOVO USUÁRIO
        cursor.execute('DIGITE AQUI O COMANDO PARA INSERIR UM NOVO USUÁRIO')
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()

def criar_projeto(id_usuario,destino,data_prevista,status,imagem,gastos,dinheiro_guardado):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('''INSERT INTO projetos_de_viagem(id_usuario,destino,data_prevista,
                       status,imagem,gastos,dinheiro_guardado) values (?, ?, ? , ?, ?, ?, ?)'''
                       ,(id_usuario,destino,data_prevista,status,imagem,gastos,dinheiro_guardado))
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()  

def buscar_viagens(id_usuario):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    # PREENCHA AQUI, BUSCAR TODAS AS VIAGENS ordem: destino, data prevista, status, imagem
    cursor.execute("DIGITE AQUI O COMANDO PARA BUSCAR AS VIAGENS")
    viagens = cursor.fetchall()
    conexao.close()

    return viagens

if __name__ == '__main__': 
    conexao = conectar_banco()
    cursos = conexao.cursor()
    usuarios = cursos.execute("select * from projetos_de_viagem where id_usuario = ?",("Gustavo@gmail.com"))
    for linha in cursos.fetchall():
        print (linha)
    # criar_projeto('Gustavo@gmail.com', 'Parana', '23/12/2026', 'Não começou', 'imagem.png',300 ,150)
    # criar_projeto('Gustavo@gmail.com', 'Paris', '19/08/2026', 'Não começou', 'imagem.png',5000 ,3000)
    # criar_projeto('geovani@gmail.com', 'Paris', '19/08/2026', 'Não começou', 'imagem.png',5000 ,3000)


    

           
        
 

    

    

