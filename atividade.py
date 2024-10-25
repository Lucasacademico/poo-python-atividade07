class Aluno:
    def __init__(self, nome_aluno, matricula):
        self.nome_aluno = nome_aluno
        self.matricula = matricula

    def mostrar_info(self):
        print(f'Aluno: {self.nome_aluno}, Matrícula: {self.matricula}')


class Curso:
    def __init__(self, nome_curso, cod_curso):
        self.nome_curso = nome_curso
        self.cod_curso = cod_curso
        self.alunos = []  

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def mostrar_alunos(self):
        print(f'Alunos matriculados no curso {self.nome_curso} ({self.cod_curso}):')
        for aluno in self.alunos:
            aluno.mostrar_info()

    def mostrar_info(self):
        print(f'Curso: {self.nome_curso}, Código: {self.cod_curso}')


class Escola:
    def __init__(self, nome_escola):
        self.nome_escola = nome_escola
        self.cursos = []

    def adicionar_curso(self, curso):
        self.cursos.append(curso)

    def mostrar_cursos(self):
        print(f'Cursos oferecidos na escola {self.nome_escola}:')
        for curso in self.cursos:
            curso.mostrar_info()
            curso.mostrar_alunos()


# Testando as classes
aluno1 = Aluno(nome_aluno="Alice", matricula="1001")
aluno2 = Aluno(nome_aluno="Bob", matricula="1002")

curso1 = Curso(nome_curso="Programação em Python", cod_curso="PY101")
curso1.adicionar_aluno(aluno1)
curso1.adicionar_aluno(aluno2)

escola = Escola(nome_escola="Escola de Tecnologia")
escola.adicionar_curso(curso1)
escola.mostrar_cursos()
