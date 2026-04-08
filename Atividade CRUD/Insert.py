# Script para inserir um novo aluno no banco de dados
from Conexao import conectar_banco

# Função para cadastrar um aluno
def cadastrar_aluno():
    # Conecta ao banco
    conn = conectar_banco()

    if conn:
        cursor = conn.cursor()

        print("\n--- Cadastro de Aluno ---")

        # Coleta os dados do aluno
        nome = input("Nome: ")
        data = input("Data de nascimento: ")
        cpf = input("CPF: ")

        # Comando do SQL para inserir
        sql = """
        INSERT INTO alunos (nome, data_nascimento, cpf)
        VALUES (%s, %s, %s)
        """

        cursor.execute(sql, (nome, data, cpf))
        conn.commit()

        print("\nAluno cadastrado com sucesso!")

        cursor.close()
        conn.close()

if __name__ == "__main__":
    cadastrar_aluno()
  