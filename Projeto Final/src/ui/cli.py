

from src.notas import Notas
from src.repository import AlunoRepository


class CLI:
    aluno_repository: AlunoRepository

    def __init__(self, aluno_repository: AlunoRepository) -> None:
        """"""
        self.aluno_repository = aluno_repository

    def run(self) -> None:
        """"""
        self._show_menu()

    def _get_user_option(self) -> str:
        """"""
        user_option = input("Digite a opção desejada: ")
        print()
        return user_option

    def _show_invalid_option(self, user_option: str) -> None:
        """"""
        print()
        print(f"Desculpe, mas a opção digitada '{user_option}' é invalida. Por favor, tente novamente.")

    def _show_bye(self) -> None:
        """"""
        print()
        print("Obrigado por usar nosso programa! Até mais ;)")

    def _show_menu(self) -> None:
        """"""
        print('Bem vindo ao Portal do INATEL - S202\n')
        print('Digite 1 se for aluno, 2 se for professor e 0 para sair.')

        user_option = self._get_user_option()

        if user_option == "0":
            return self._show_bye()

        if user_option == "1":
            print("Bem vindo aluno de Banco de Dados!")
            return self._show_menu_aluno()

        if user_option == "2":
            print("Bem vindo professor de Banco de Dados!")
            return self._show_menu_professor()

        self._show_invalid_option(user_option)
        return self._show_menu()

    def _show_menu_aluno(self) -> None:
        """"""

    def _show_menu_professor(self) -> None:
        """"""
        print("""
        Menu professor:
            1 - Adicionar aluno
            2 - Ver aluno
            3 - Ver alunos
            4 - Atualizar nota da NP1
            5 - Atualizar nota da NP2
            6 - Deletar aluno
            0 - Sair
        """
        )

        user_option = self._get_user_option()

        if user_option == "0":
            return self._show_bye()

        if user_option == "1":
            self._create_aluno()
            return self._show_menu_professor()

        if user_option == "2":
            self._read_aluno()
            return self._show_menu_professor()

        if user_option == "3":
            self._read_all_alunos()
            return self._show_menu_professor()

        if user_option == "4":
            self._update_aluno_np1()
            return self._show_menu_professor()

        if user_option == "5":
            self._update_aluno_np2()
            return self._show_menu_professor()

        if user_option == "6":
            self._delete_aluno()
            return self._show_menu_professor()

        self._show_invalid_option(user_option)
        return self._show_menu_professor()

    def _create_aluno(self) -> None:
        """"""
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite a matricula do aluno: ")
        np1 = float(input("Digite a NP1 do aluno: "))
        np2 = float(input("Digite a NP2 do aluno: "))

        notas_aluno = Notas(np1, np2)
        
        self.aluno_repository.create(nome, matricula, notas_aluno)

        print("Aluno criado com sucesso!")

    def _read_aluno(self) -> None:
        """"""
        matricula = input("Digite a matricula do aluno: ")

        aluno = self.aluno_repository.read(matricula)

        print("Aluno:", end="\n\n")
        print(aluno)

    def _read_all_alunos(self) -> None:
        """"""
        alunos = self.aluno_repository.read_all()

        print("Alunos:", end="\n\n")
        print(alunos)

    def _update_aluno_np1(self) -> None:
        """"""
        matricula = input("Digite a matricula do aluno: ")
        np1 = float(input("Digite a nova nota NP1 do aluno: "))

        self.aluno_repository.update_np1(matricula, np1)

        print(f"Nota NP1 do aluno atualizada para {np1}!")

    def _update_aluno_np2(self) -> None:
        """"""
        matricula = input("Digite a matricula do aluno: ")
        np2 = float(input("Digite a nova nota NP2 do aluno: "))

        self.aluno_repository.update_np1(matricula, np2)

        print(f"Nota NP1 do aluno atualizada para {np2}!")

    def _delete_aluno(self) -> None:
        """"""
        matricula = input("Digite a matricula do aluno: ")

        response = self.aluno_repository.delete(matricula)
        print('RESPONSE: ', response)

        print(f"Aluno da matrícula {matricula} foi removido!")
