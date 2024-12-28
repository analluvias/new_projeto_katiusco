
def visualizar_professores():
    from repository.repositories import ProfessorRepository
    prof_repo = ProfessorRepository()

    # Executar o metodo get_perfil
    professores = prof_repo.get_all_professores()
    print(professores)

    # Certifique-se de fechar a conexão ao finalizar
    prof_repo.close_connection()


def interface():

    print("**********************************\n")
    print("        BEM-VINDO                   ")
    print("**********************************\n")
    while True:
        opcao = input(
            "Selecione uma opção abaixo:\n" 
            "(1) Visualizar perfil dos professores\n" 
            "(2) Visualizar resumo do perfil dos alunos\n" 
            "(3) Cadastrar seu perfil\n" 
            "(4) Editar seu perfil\n" 
            "(5) Inserir sugestão de perfil para professor\n" 
            "(6) Inserir sugestão para o sistema\n")

        if opcao == '1':
            visualizar_professores()
        if opcao == '2':
            pass
        if opcao == '3':
            pass
        if opcao == '4':
            pass
        if opcao == '5':
            pass
        if opcao == '6':
            pass
        else:
            pass
