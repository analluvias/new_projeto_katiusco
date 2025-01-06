from datetime import datetime

from entity.ExperienciaProfissional import ExperienciaProfissional


def visualizar_professores():
    from facade.facade import Facade

    facade = Facade()

    opcao = input("\n\nComo você deseja visualizar os professores?\n\n" 
                  "1. Todos os professores\n" 
                  "2. Por área de conhecimento\n" 
                  "3. Por projeto\n" 
                  "Digite o número da opção: ")

    facade.exibir_professores(opcao)


def visualizar_alunos():
    from facade.facade import Facade

    opcao = input("Como você deseja visualizar os alunos?\n\n"
                  "1. Todos os alunos\n"
                  "2. Por área de interesse\n"
                  "3. Por curso\n"
                  "4. Por projeto participado\n\n"
                  "Digite o número da opção: ")

    facade = Facade()
    facade.exibir_alunos(opcao)


def inserir_areas_interesse():
    from facade.facade import Facade

    facade = Facade()

    areas = facade.exibir_areas()
    for area in areas:
        print(f'{area[0]}. {area[1]}')

    areas_input = input("Digite o número das suas áreas de interesse, separe por espaços:\n")
    # Divide a string de entrada em elementos separados por espaços
    areas_selecionadas = areas_input.split()
    # Filtra os elementos para incluir apenas números
    areas_selecionadas = [int(numero) for numero in areas_selecionadas if numero.isdigit()]

    return areas_selecionadas



def cadastrar_aluno():
    from facade.facade import Facade
    import getpass

    facade = Facade()

    cursos = ['engenharia de computação',
              'telemática',
              'técnico em informática']
    experiencias_profissionais = []

    while True:
        nome = input("\nDigite seu nome completo: ")
        r = input(f"Seu nome é '{nome}'?\n(digite y para"
                  f" confirmar ou qualquer outra tecla para digitar novamente)")
        if r == 'y':
            break

    while True:
        curso = input( f"\nSelecione o seu curso (Digite um numero de 1 a 3): \n"
                  f"1. Engenharia de Computação\n"
                  f"2. Telemática\n"
                  f"3. Técnico em Informática\n")

        if 1 <= int(curso) <= 3:
            confirma = input(f"Você estuda '{cursos[int(curso)-1]}'?\nDigite y para"
                             " confirmar e qualquer outra tecla para digitar novamente ")

            if confirma == 'y':
                break

    while True:
        email = input("\nDigite seu email academico sem o domínio (@academico.ifpb.edu.br): ")
        email = email + '@academico.ifpb.edu.br'
        r = input(f"Seu email é '{email}'?\nDigite y para"
                  f" confirmar ou qualquer outra tecla para digitar novamente ")
        if r == 'y':
            break

    while True:
        periodo = input("\nDigite o período em que você está matriculado: ")

        r = input(f"Confirme, você está no {periodo}° período?\nDigite y para"
                  f" confirmar ou qualquer outra tecla para digitar novamente ")
        if r == 'y':
            break


    while True:
        senha1 = getpass.getpass(f"\nDigite a senha desejada: ")
        senha2 = getpass.getpass(f"\nConfirme sua senha: ")

        if senha1 == senha2:
            break
        else:
            print(f'\n\n*senha incorreta*\n\n')


    print("\n\nAgora vamos cadastrar seus interesses e experiências.\n\n")
    while True:

        while True:
            titulo = input("Insira o título da experiência profissional: ")
            r = input(f"\n{titulo}?\nDigite y para confirmar e qualquer outra tecla para digitar novamente. ")
            if r == 'y':
                break

        while True:
            try:
                dia_inicio = input("Informe o dia da data de início: ")
                mes_inicio = input("Informe o mês da data de início: ")
                ano_inicio = input("Informe o ano da data de início: ")

                # Formatando a data
                data_inicio = f"{dia_inicio}/{mes_inicio}/{ano_inicio}"
                formato = "%d/%m/%Y"  # Formato de data esperado
                data_inicio_dt = datetime.strptime(data_inicio, formato)

                r = input(f"{data_inicio}?\nDigite y para confirmar e qualquer outra tecla para digitar novamente.")
                if r == 'y':
                    print("Data criada com sucesso:", data_inicio_dt)
                    break

            except ValueError:
                print("Data inválida. Por favor, tente novamente.")

        while True:
            try:
                dia_fim = input("Informe o dia da data final: ")
                mes_fim = input("Informe o mês da data final:")
                ano_fim = input("Informe o ano da data final:")

                # Formatando a data
                data_fim = f"{dia_fim}/{mes_fim}/{ano_fim}"
                formato = "%d/%m/%Y"  # Formato de data esperado
                data_fim_dt = datetime.strptime(data_fim, formato)

                r = input(f"{dia_fim}/{mes_fim}/{ano_fim}?\n"
                          f"Digite y para confirmar e qualquer outra tecla para digitar novamente.")
                if r == 'y':
                    break

            except ValueError:
                print("Data inválida. Por favor, tente novamente.")

        while True:
            descricao = input("Insira um breve texto de descrição da sua experiência:\n")

            r = input(f"Digite y para confirmar e qualquer outra tecla para digitar novamente.")
            if r == 'y':
                break

        experiencias_profissionais.append(ExperienciaProfissional(None, titulo, data_inicio_dt, data_fim_dt, descricao))

        r = input("\n\nDeseja inserir outra experiência?\nDigite 'y' para sim  e qualquer outra tecla para não.\n")

        if r != 'y':
            break
    
    print("\n\nCadastre também suas áreas de interesse\n\n")
    areas_interesse = inserir_areas_interesse()

    print('\n\nPor último, selecione os projetos participados:\n\n')
    projetos = inserir_projetos()

    facade.criar_aluno(nome, cursos[int(curso)-1], email, periodo, senha1, experiencias_profissionais, areas_interesse, projetos)


def inserir_projetos():
    from facade.facade import Facade

    facade = Facade()
    projetos = facade.exibir_projetos()
    for projeto in projetos:
        print(f'{projeto[0]}. {projeto[1]}')

    projetos_input = input("Digite o número dos projetos que já participou, separe por espaços:\n")
    # Divide a string de entrada em elementos separados por espaços
    proj_selecionados = projetos_input.split()
    # Filtra os elementos para incluir apenas números
    proj_selecionados = [int(numero) for numero in proj_selecionados if numero.isdigit()]

    return proj_selecionados


def interface():

    print("**********************************\n")
    print("        BEM-VINDO                   ")
    print("**********************************\n")
    while True:
        opcao = input(
            "Selecione uma opção abaixo:\n" 
            "(1) Visualizar vitrine dos professores\n" 
            "(2) Visualizar vitrine dos alunos\n" 
            "(3) Cadastrar sua vitrine\n" 
            "(4) Editar sua vitrine\n" 
            "(5) Inserir sugestão de vitrine para professor\n" 
            "(6) Inserir sugestão para o sistema\n")

        if opcao == '1':
            visualizar_professores()
        if opcao == '2':
            visualizar_alunos()
        if opcao == '3':
            cadastrar_aluno()
            # inserir_areas_interesse()
            # inserir_projetos()
        if opcao == '4':
            pass
        if opcao == '5':
            pass
        if opcao == '6':
            pass
        else:
            pass
