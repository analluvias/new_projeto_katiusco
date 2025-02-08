# main/facade/facade.py

from entity.Aluno import Aluno
from entity.Perfil import Perfil
from entity.ExperienciaProfissional import ExperienciaProfissional
from entity.SugestaoNovoProfessor import SugestaoNovoProfessor
from repository.repositories import (
    ProfessorRepository,
    AlunoRepository,
    PerfilRepository,
    ExperienciaProfissionalRepository,
    ProjetoRepository,
    GrandeAreaRepository,
    CursoRepository
)

from datetime import datetime
import psycopg2.errors

from repository.repositories import SugestaoNovoProfessorRepository


class Facade:

    def inserir_sugestao_professor(self, nome):
        repository = SugestaoNovoProfessorRepository()
        sugestao = SugestaoNovoProfessor(datetime.now().date(), nome)
        repository.add_sugestao(sugestao)

    def apagar_projeto_participado_por_email(self, email, projetos):
        alunoRepository = AlunoRepository()
        aluno = alunoRepository.get_aluno_by_email(email)
        id = aluno[0]

        for projeto in projetos:
            alunoRepository.remove_projeto_from_aluno(id, projeto)

    def inserir_projeto_participado_por_email(self, email, projetos):
        alunoRepository = AlunoRepository()
        aluno = alunoRepository.get_aluno_by_email(email)
        id = aluno[0]

        try:
            for projeto in projetos:
                alunoRepository.add_projeto_to_aluno(id, projeto)
        except psycopg2.errors.UniqueViolation as e:
            print("\nVocê já Participa do projeto. Selecione outro.\n")

    def apagar_area_interesse_por_email(self, email, areas_interesse):
        alunoRepository = AlunoRepository()
        aluno = alunoRepository.get_aluno_by_email(email)
        id = aluno[0]

        for area in areas_interesse:
            alunoRepository.remove_grande_area_from_aluno(id, area)

    def inserir_areas_interesse_por_email(self, email, areas_interesse):
        alunoRepository = AlunoRepository()
        aluno = alunoRepository.get_aluno_by_email(email)
        id = aluno[0]

        try:
            for area in areas_interesse:
                alunoRepository.add_grande_area_to_aluno(id, area)
        except psycopg2.errors.UniqueViolation as e:
            print("\nVocê já demonstrou interesse na área. Selecione outra.\n")


    def apagar_experiencia(self, id):
        repository = ExperienciaProfissionalRepository()
        repository.delete_experiencia(id)

    def update_senha_by_email(self, email, senha):
        repository = AlunoRepository()
        repository.update_senha_by_email(email, senha)

    def update_periodo_by_email(self, email, periodo):
        repository = AlunoRepository()
        repository.update_periodo_by_email(email, periodo)

    def update_curso_by_email(self, email, curso):
        repository = PerfilRepository()
        repository.update_curso_by_email(email, curso)


    def update_nome_by_email(self, email, nome):
        repository = PerfilRepository()
        repository.update_nome_by_email(email, nome)


    def exibir_professores(self, opcao):
        repository = ProfessorRepository()
        professores = repository.get_all_professores()

        if opcao == '1':
            for professor in professores:
                self.exibir_detalhes_professor(professor)
        elif opcao == '2':
            areas = self.exibir_areas()
            self.exibir_opcoes(areas, "Escolha a área de conhecimento")
            area_index = self.obter_opcao_valida(areas)
            selected_area = areas[int(area_index) - 1][1]

            for professor in professores:
                if selected_area in professor[5]:
                    self.exibir_detalhes_professor(professor)
        elif opcao == '3':
            projetos = self.exibir_projetos()
            self.exibir_opcoes(projetos, "Digite o índice do projeto desejado")
            proj_index = self.obter_opcao_valida(projetos)
            selected_projeto = projetos[int(proj_index) - 1][1]

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

    def exibir_aluno(self, email):
        repository = AlunoRepository()
        aluno = repository.get_aluno_by_email(email)
        self.exibir_detalhes_aluno(aluno)

    def exibir_alunos(self, opcao):
        repository = AlunoRepository()
        alunos = repository.get_all_alunos()

        if opcao == '1':
            for aluno in alunos:
                self.exibir_detalhes_aluno(aluno)
        elif opcao == '2':
            areas = self.exibir_areas()
            self.exibir_opcoes(areas, "Escolha a área de interesse")
            area_index = self.obter_opcao_valida(areas)
            selected_area = areas[int(area_index) - 1][1]

            for aluno in alunos:
                if selected_area in aluno[7]:
                    self.exibir_detalhes_aluno(aluno)
        elif opcao == '3':
            cursos = self.exibir_cursos()
            self.exibir_opcoes(cursos, "Digite o índice do curso desejado")
            curso_index = self.obter_opcao_valida(cursos)
            selected_curso = cursos[int(curso_index) - 1][1]

            for aluno in alunos:
                if selected_curso == aluno[2]:
                    self.exibir_detalhes_aluno(aluno)
        elif opcao == '4':
            projetos = self.exibir_projetos()
            self.exibir_opcoes(projetos, "Digite o índice do projeto desejado")
            proj_index = self.obter_opcao_valida(projetos)
            selected_projeto = projetos[int(proj_index) - 1][1]

            for aluno in alunos:
                if selected_projeto in aluno[8]:
                    self.exibir_detalhes_aluno(aluno)
        else:
            print("Opção inválida. Tente novamente.")

    def criar_experiencia_profissional_aluno_by_email(self, email, titulo, data_inicio, data_fim, descricao):
        try:
            self.verifica_datas(data_inicio, data_fim)
            alunoRepository = AlunoRepository()
            aluno = alunoRepository.get_aluno_by_email(email)
            id = aluno[0]
            repository = ExperienciaProfissionalRepository()
            experiencia = ExperienciaProfissional(None, titulo, data_inicio, data_fim, descricao)
            repository.add_experiencia(experiencia, id)
        except ValueError as e:
            print(f"Erro: {e}")

    def criar_experiencia_profissional_aluno(self, id, titulo, data_inicio, data_fim, descricao):
        try:
            self.verifica_datas(data_inicio, data_fim)
            repository = ExperienciaProfissionalRepository()
            experiencia = ExperienciaProfissional(None, titulo, data_inicio, data_fim, descricao)
            repository.add_experiencia(experiencia, id)
        except ValueError as e:
            print(f"Erro: {e}")

    def criar_aluno(self, nome, curso, email_institucional, periodo, senha, experiencias_profissionais, areas_interesse,
                    projetos):
        try:
            self.verifica_email_institucional(email_institucional)
            perfil = Perfil(None, nome, curso, email_institucional)
            repo_perfil = PerfilRepository()
            id_perfil = repo_perfil.add_perfil(perfil)
        except ValueError as e:
            print(f"Erro ao criar aluno: {e}")
            return

        try:
            self.verificar_periodo(periodo)
            self.verificar_senha(senha)
            aluno = Aluno(None, nome, curso, email_institucional, periodo, senha)

            for experiencia in experiencias_profissionais:
                aluno.add_experiencia_profissional(experiencia)
            for area in areas_interesse:
                aluno.add_grande_area(area)
            for projeto in projetos:
                aluno.add_projeto(projeto)

            repo_aluno = AlunoRepository()
            id_aluno = repo_aluno.add_aluno(aluno, id_perfil)
            return id_aluno
        except ValueError as e:
            print(f"Erro ao criar aluno: {e}")
            return

    def verifica_datas(self, data_inicio, data_fim):
        formato = "%d/%m/%Y"
        data_inicio_dt = datetime.strptime(data_inicio, formato)
        data_fim_dt = datetime.strptime(data_fim, formato)
        if data_inicio_dt > data_fim_dt:
            raise ValueError("Data inicial maior que a data final.")

    def verificar_senha(self, senha):
        if len(senha) < 5:
            raise ValueError("Senha deve ter pelo menos 5 caracteres.")

    def verificar_periodo(self, periodo):
        if not (1 <= int(periodo) <= 10):
            raise ValueError("Período inválido.")

    def verifica_email_institucional(self, email):
        if '@academico.ifpb.edu.br' not in email:
            raise ValueError("Email institucional incorreto.")

    def exibir_opcoes(self, opcoes, mensagem):
        print(mensagem)
        for opcao in opcoes:
            print(f'{opcao[0]}. {opcao[1]}')

    def obter_opcao_valida(self, lista):
        opcao = input("Escolha uma opção: ")
        if not opcao.isdigit() or int(opcao) not in range(1, len(lista) + 1):
            print("Opção inválida, selecionando a primeira opção por padrão.")
            return '1'
        return opcao

    def exibir_projetos(self):
        return ProjetoRepository().get_all_projetos()

    def exibir_areas(self):
        return GrandeAreaRepository().get_all_grande_areas()

    def exibir_cursos(self):
        return CursoRepository().get_all_cursos()

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
                print(f"  ID: {estagio['id']}")
                print(f"  Título: {estagio['titulo']}")
                print(f"  Data de Início: {estagio['data_inicio']}")
                print(f"  Data de Fim: {estagio['data_fim']}")
                print(f"  Descrição: {estagio['descricao']}\n")

        print("-" * 40)
