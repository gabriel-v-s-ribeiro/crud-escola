
# Script para gerenciar conexão com banco de dados MySQL
import mysql.connector
from mysql.connector import Error

# Função para estabelecer conexão com o banco de dados MySQL
def conectar_banco():
    try:
        # Conexão
        conexao = mysql.connector.connect(
            host='localhost',
            database='escola',
            user='root',
            password='Tacasiri2007@'
        )

        if conexao.is_connected():
            print("Conectado")

        return conexao
    
    except Error as e:
        # Em caso de erro, exibe mensagem de erro
        print(f"Erro ao conectar: {e}")
        return None

# Chama a função quando o script é executado
if __name__ == "__main__":
    conectar_banco()