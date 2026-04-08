# Script principal do sistema do Banco de Dados
from Insert import cadastrar_aluno;
from Select import listar_alunos;
from Update import atualizar_aluno;
from Delete import deletar_aluno;

# Função para exibir o menu e gerenciar as opções
def menu(): 
    # Loop infinito para o menu para realizar várias operações
    while True: # Exibe o menu de opções para o usuário
        print(""" 
=================================
        SISTEMA ESCOLA
=================================

1 - Cadastrar aluno
2 - Listar alunos
3 - Atualizar aluno
4 - Excluir aluno
5 - Sair
""") # Pede para escolher uma opção

        opcao = input("Escolha uma opção: ")

        # Verifica a opção escolhida
        if opcao == "1": # Opção para cadastrar um aluno
            cadastrar_aluno()

        elif opcao == "2": # Opção para listar os alunos
            listar_alunos()

        elif opcao == "3": # Opção para atualizar um aluno
            atualizar_aluno()

        elif opcao == "4": # Opção para deletar um aluno
            deletar_aluno()

        elif opcao == "5": # Opção para sair do sistema
            print("Encerrando sistema...")
            break # Encerra o loop e o programa

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()