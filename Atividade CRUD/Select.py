# Script para listar alunos do banco de dados
from Conexao import conectar_banco

# Função para listar todos os alunos
def listar_alunos():
    # Conecta ao banco
    conn = conectar_banco()

    if conn:
        cursor = conn.cursor()

        # Executa a consulta para selecionar todos os alunos ordenados por nome
        cursor.execute("SELECT * FROM alunos ORDER BY nome")

        alunos = cursor.fetchall()

        print("\n======================================================")
        print("                     LISTA DE ALUNOS")
        print("======================================================")

        print(f"{'ID':<5}{'NOME':<20}{'DATA NASC':<15}{'CPF':<15}")
        print("------------------------------------------------------")

        # Itera sobre os resultados e imprime
        for aluno in alunos:
            print(f"{aluno[0]:<5}{aluno[1]:<20}{aluno[2]:<15}{aluno[3]:<15}")

        print("======================================================")

        cursor.close()
        conn.close()
if __name__ == "__main__":
    listar_alunos()