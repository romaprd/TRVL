import sqlite3

def conectar_banco():
    conexao = sqlite3.connect("trvl.db")
    return conexao 

def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''create table if not exists usuarios
                   (email text primary key,nome text,senha text)''')
    
    cursor.execute('''create table if not exists usuarios_projetos
                   (id integer primary key, email_usuario text, id_projeto integer)''')
    
    cursor.execute('''create table if not exists projetos_de_viagem
                   (id integer primary key,id_usuario text,destino text,data_prevista text,
                   status text,imagem text,gastos real,dinheiro_guardado real)''')
    
    conexao.commit()

def criar_usuario(email, nome, senha):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        # PREENCHA AQUI - QUAL O COMANDO CRIAR UM NOVO USUÁRIO
        cursor.execute('insert into usuarios(email, nome, senha) VALUES (?, ?, ?)', (email, nome, senha))
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()
        
def adc_new_usuario(email, idprojeto):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        # PREENCHA AQUI - QUAL O COMANDO CRIAR UM NOVO USUÁRIO
        cursor.execute('insert into usuarios_projetos(email_usuario, id_projeto) VALUES (?, ?)', (email, idprojeto))
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()
        
def mudar_nome_usuario(nome, email):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        #codigo para alterar o nome do usuario
        cursor.execute('UPDATE usuarios SET nome = ? WHERE email = ?',(nome, email,))
        conexao.commit()
        viagens = cursor.fetchall()
        return viagens
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()
        
def mudar_senha_usuario(senha, email):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        #codigo para alterar o nome do usuario
        cursor.execute('UPDATE usuarios SET senha = ? WHERE email = ?',(senha, email,))
        conexao.commit()
        viagens = cursor.fetchall()
        return viagens
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
    # PREENCHA AQUI, BUSCAR TODAS AS VIAGENS ordem: destino, data_prevista, status, imagem
    cursor.execute("SELECT destino, data_prevista, status, imagem, id FROM projetos_de_viagem WHERE id_usuario = ?", (id_usuario,))
    viagens = cursor.fetchall()
    conexao.close()

    return viagens

def apagar_viagem(id_viagem):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        # PREENCHA AQUI - QUAL O COMANDO CRIAR UM NOVO USUÁRIO
        cursor.execute('DELETE FROM projetos_de_viagem WHERE id = ?', id_viagem)
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()
        
def mostrar_id_viagens(id_email):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        # PREENCHA AQUI - QUAL O COMANDO CRIAR UM NOVO USUÁRIO
        cursor.execute('SELECT * FROM projetos_de_viagem WHERE id_usuario = ?', (id_email,))
        conexao.commit()
        viagens = cursor.fetchall()
        return viagens 
    
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()
        
def editar_viagem(destino,data_prevista,status,imagem,gastos,dinheiro_guardado, id_usuario):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        #codigo para alterar o nome do usuario
        cursor.execute('UPDATE projetos_de_viagem SET destino = ?, data_prevista = ?, status = ?, imagem = ?, gastos = ?, dinheiro_guardado = ? WHERE id_usuario = ?',(destino, data_prevista, status, imagem, gastos, dinheiro_guardado, id_usuario,))
        conexao.commit()
        viagens = cursor.fetchall()
        return viagens
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()
        
def apagar_usuario(usuarios):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        # PREENCHA AQUI - QUAL O COMANDO CRIAR UM NOVO USUÁRIO
        cursor.execute('DELETE FROM usuarios WHERE email = ?',(usuarios,))
        
        #apaga todas as viagens criadas por ela
        cursor.execute('DELETE FROM projetos_de_viagem WHERE id_usuario = ?',(usuarios,))
         
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()

if __name__ == '__main__': 
    conexao = conectar_banco()
    criar_tabelas()
    id_viagens = mostrar_id_viagens("deyvysilva2006@gmail.com")
    print(id_viagens)
    
    adc_new_usuario("deyvyalex2006@gmail.com", 1)
    # editar_viagem("mosqueiro", "09/05/2025", "planejado", "https://www.passeios.org/wp-content/uploads/2022/07/01_3-1.jpg", "10.000.00", "12.000.00", "deyvysilva2006@gmail.com")
    # mudar_nome_usuario("romario", "deyvysilva2006@gmail.com")
    # mudar_senha_usuario("13579", "deyvysilva2006@gmail.com")
    # apagar_viagem("1")
    
    # apagar_usuario("rodfsjanvjsanf@gmail.com")
    
    # SELECT projetos_de_viagem.destino FROM projetos_de_viagem, usuarios_projetos WHERE projetos_de_viagem.id = usuarios_projetos.id_projeto AND usuarios_projetos.email_usuario = 'deyvyalex2006@gmail.com'