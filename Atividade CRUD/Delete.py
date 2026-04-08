# Script para deletar um aluno do banco de dados
from Conexao import conectar_banco

# Função De deletar um aluno pelo ID
def deletar_aluno():
    # Conecta ao banco
    conn = conectar_banco()

    if conn:
        cursor = conn.cursor()

        # Solicita o ID do aluno a ser deletado
        id_aluno = input("Digite o ID do aluno que deseja excluir: ")

        # Comando do SQL para deletar
        sql = "DELETE FROM alunos WHERE id = %s"

        cursor.execute(sql, (id_aluno,))
        conn.commit()

        print("Aluno excluído com sucesso!")

        cursor.close()
        conn.close()
    else:
        print("Falha na conexão")
if __name__ == "__main__":
    deletar_aluno()
