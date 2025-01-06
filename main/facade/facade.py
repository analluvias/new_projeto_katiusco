from entity.Aluno import Aluno
from entity.Perfil import Perfil
from entity.ExperienciaProfissional import ExperienciaProfissional
import emailable
from datetime import datetime


def verifica_datas(data_inicio, data_fim):
    formato = "%d/%m/%Y" # Ajuste o formato conforme necessário
    data_inicio_dt = datetime.strptime(data_inicio, formato)
    data_fim_dt = datetime.strptime(data_fim, formato)

    if data_inicio_dt > data_fim_dt:
        raise ValueError("Data inicial maior que a data final.")

    return


class Facade:

    def exibir_professores(self, opcao):
        from repository.repositories import ProfessorRepository

        repository = ProfessorRepository()
        professores = repository.get_all_professores()

        if opcao == '1':
            for professor in professores:
                self.exibir_detalhes_professor(professor)
        elif opcao == '2':
            areas = self.exibir_areas()
            for a in areas: print(f'{a[0]}. {a[1]}')
            area_index = input("Escolha a área de conhecimento (digite o índice): ")
            if not area_index.isdigit() or int(area_index) not in range(1, len(areas) + 1):
                print("Opção inválida, selecionando a primeira área por padrão.")
                area_index = '1'
            selected_area = areas[int(area_index) - 1][1]

            for professor in professores:
                if selected_area in professor[5]:
                    self.exibir_detalhes_professor(professor)
        elif opcao == '3':
            projetos = self.exibir_projetos()
            for p in projetos:
                print(f'{p[0]}. {p[1]}')
            proj_index = input("Digite o índice do projeto desejado: ")

            # Verifica se a opção é um número e se está no intervalo válido
            if not proj_index.isdigit() or int(proj_index) not in range(1, len(projetos) + 1):
                print("Opção inválida, selecionando a primeira área por padrão.")
                proj_index = '1'  # Seleciona o índice 0, que é equivalente à primeira área (índice 1)

            # Obtém o valor da área selecionada a partir do índice
            selected_projeto = projetos[int(proj_index) - 1][1]  # Subtrai 1 porque os índices da lista começam em 0

            for professor in professores:
                if selected_projeto in professor[6]:
                    self.exibir_detalhes_professor(professor)
        else:
            print("Opção inválida. Tente novamente.")

    def exibir_detalhes_professor(self, professor):
        print(f"\n\nID: {professor[0]}")
        print(f"Nome: {professor[1]}")
        print(f"Disciplina: {professor[2]}")
        print(f"Email: {professor[3]}")
        print(f"Sala: {professor[4]}")
        print(f"Áreas de conhecimento: {', '.join(professor[5])}")
        print(f"Projetos: {', '.join(professor[6])}")
        print("-" * 40)


    def exibir_detalhes_aluno(self, aluno):
        print(f"\n\nID: {aluno[0]}")
        print(f"Nome: {aluno[1]}")
        print(f"Curso: {aluno[2]}")
        print(f"Email: {aluno[3]}")
        print(f"Período: {aluno[4]}")
        print(f"Senha: {aluno[5]}")
        print(f"Áreas de interesse: {', '.join(aluno[7])}")
        print(f"Projetos: {', '.join(aluno[8])}")

        # Exibindo estágios (se houver)
        if aluno[6]:
            print("Estágios:")
            for estagio in aluno[6]:
                print(f"  Título: {estagio['titulo']}")
                print(f"  Data de Início: {estagio['data_inicio']}")
                print(f"  Data de Fim: {estagio['data_fim']}")
                print(f"  Descrição: {estagio['descricao']}")

        print("-" * 40)


    def exibir_alunos(self, opcao):
        from repository.repositories import AlunoRepository

        repository = AlunoRepository()
        alunos = repository.get_all_alunos()

        if opcao == '1':
            for aluno in alunos:
                self.exibir_detalhes_aluno(aluno)
        elif opcao == '2':

            areas = self.exibir_areas()
            for a in areas:
                print(f'{a[0]}. {a[1]}')
            area_index = input("Escolha a área de interesse (digite o índice): ")
            # Verifica se a opção é um número e se está no intervalo válido
            if not area_index.isdigit() or int(area_index) not in range(1, len(areas) + 1):
                print("Opção inválida, selecionando a primeira área por padrão.")
                area_index = '1'  # Seleciona o índice 0, que é equivalente à primeira área (índice 1)
            # Obtém o valor da área selecionada a partir do índice
            selected_area = areas[int(area_index) - 1][1]  # Subtrai 1 porque os índices da lista começam em 0

            for aluno in alunos:
                if selected_area in aluno[7]:
                    self.exibir_detalhes_aluno(aluno)

        elif opcao == '3':

            cursos = self.exibir_cursos()
            for c in cursos:
                print(f'{c[0]}. {c[1]}')
            curso_index = input("Digite o índice do curso desejado: ")

            # Verifica se a opção é um número e se está no intervalo válido
            if not curso_index.isdigit() or int(curso_index) not in range(1, len(cursos) + 1):
                print("Opção inválida, selecionando a primeira área por padrão.")
                curso_index = '1'  # Seleciona o índice 0, que é equivalente à primeira área (índice 1)

            # Obtém o valor da área selecionada a partir do índice
            selected_curso = cursos[int(curso_index) - 1][1]  # Subtrai 1 porque os índices da lista começam em 0

            for aluno in alunos:
                if selected_curso == aluno[2]:
                    self.exibir_detalhes_aluno(aluno)

        elif opcao == '4':
            projetos = self.exibir_projetos()
            for p in projetos:
                print(f'{p[0]}. {p[1]}')
            proj_index = input("Digite o índice do projeto desejado: ")

            # Verifica se a opção é um número e se está no intervalo válido
            if not proj_index.isdigit() or int(proj_index) not in range(1, len(projetos) + 1):
                print("Opção inválida, selecionando a primeira área por padrão.")
                proj_index = '1'  # Seleciona o índice 0, que é equivalente à primeira área (índice 1)

            # Obtém o valor da área selecionada a partir do índice
            selected_projeto = projetos[int(proj_index) - 1][1]  # Subtrai 1 porque os índices da lista começam em 0

            for aluno in alunos:
                if selected_projeto in aluno[8]:
                    self.exibir_detalhes_aluno(aluno)
        else:
            print("Opção inválida. Tente novamente.")


    def exibir_projetos(self):
        from repository.repositories import ProjetoRepository
        repository = ProjetoRepository()
        return repository.get_all_projetos()


    def exibir_areas(self):
        from repository.repositories import GrandeAreaRepository
        repository = GrandeAreaRepository()
        return repository.get_all_grande_areas()


    def exibir_cursos(self):
        from repository.repositories import CursoRepository
        repository = CursoRepository()
        return repository.get_all_cursos()


    def criar_experiencia_profissional_aluno(self, id, titulo, data_inicio, data_fim, descricao):

        from repository.repositories import ExperienciaProfissionalRepository
        
        try:
            verifica_datas(data_inicio, data_fim)
            repository = ExperienciaProfissionalRepository()
            experiencia = ExperienciaProfissional(None, titulo, data_inicio, data_fim, descricao)
            repository.add_experiencia(experiencia, id)
        except:
            print("Verifique se a data início é menor que a data fim.")

    def criar_aluno(self, nome, curso, email_institucional, periodo, senha, experiencias_profissionais, areas_interesse, projetos):

        from repository.repositories import AlunoRepository, PerfilRepository

        try:
            verifica_email_institucional(email_institucional)
            perfil = Perfil(None, nome, curso, email_institucional)
            repo_perfil = PerfilRepository()
            id_perfil = repo_perfil.add_perfil(perfil)
        except:
            print("Erro ao criar aluno, verifique se todos os campos"
                  "estão preenchidos e se o email é institucional.")
            return

        try:
            print("idddd", id_perfil)
            verificar_periodo(periodo)
            verificar_senha(senha)
            aluno = Aluno(None, nome, curso, email_institucional, periodo, senha)

            for experiencia in experiencias_profissionais:
                print(experiencia)
                aluno.add_experiencia_profissional(experiencia)

            for area in areas_interesse:
                aluno.add_grande_area(area)

            for projeto in projetos:
                aluno.add_projeto(projeto)

            repo_aluno = AlunoRepository()
            id_aluno = repo_aluno.add_aluno(aluno, id_perfil)
        except:
            print("Erro ao criar aluno, verifique se o período é válido"
                  " e se a senha tem pelo menos 5 caracteres.")
            return

        return id_aluno

def verificar_senha(senha):
    if len(senha) >= 5:
        return True
    else:
        raise ValueError(f"Senha deve ter pelo menos 5 caracteres.")


def verificar_periodo(periodo):
    if 1 <= int(periodo) <= 10:
        return True
    else:
        raise ValueError(f"Período Inválido.")


def verifica_email_institucional(email):
    try:
        # client = emailable.Client('test_ae3408af24bd480f6ab3')
        # response = client.verify(email)

        # if response.state == 'deliverable' and '@academico.ifpb.edu.br' in email:
        #     return
        if '@academico.ifpb.edu.br' in email:
            return
        else:
            raise Exception('Email institucional incorreto.')
    except Exception as e:
        raise ValueError(f"Erro ao verificar o e-mail: {e}")
