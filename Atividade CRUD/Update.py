
# Script para atualizar dados de um aluno no banco de dados
from Conexao import conectar_banco

# Função para atualizar o nome de um aluno
def atualizar_aluno():
    # Conecta ao banco
    conn = conectar_banco()

    if conn:
        cursor = conn.cursor()

        # Solicita o ID e o novo nome
        id_aluno = input("Digite o ID do aluno: ")
        novo_nome = input("Novo nome: ")

        # Comando SQL para atualizar
        sql = "UPDATE alunos SET nome = %s WHERE id = %s"

        cursor.execute(sql, (novo_nome, id_aluno))
        conn.commit()

        print("Aluno atualizado com sucesso!")

        cursor.close()
        conn.close()
if __name__ == "__main__":
    atualizar_aluno()