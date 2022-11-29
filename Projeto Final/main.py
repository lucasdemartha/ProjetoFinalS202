# from pprintpp import pprint as pp
from crud import crudmenu
from db.database import Graph
from helper.write_a_json import write_a_json as wj

db = Graph(uri='bolt://54.166.33.76:7687', user='neo4j', password='cycles-facepiece-baby')

if __name__ == '__main__':

    tcrud = crudmenu()

    op = 0;

    op = int(input(f'Bem vindo ao Portal do inatel - S202'
    f'Digite 1 se for aluno ou digite 2 se for professor: '))

    aux = 0
    aux2 = 0

    if (op == 2):
        while aux2 != 0:
            aux2 = int(input(f'Bem vindo professor de Banco de Dados'
            f'Menu professor:'
            f'1 - adicionar aluno'
            f'2 - ver alunos'
            f'3 - deletar aluno'
            f'4 - atualizar nota da NP1'
            f'5 - atualizar nota da NP2'
            f'0 - Sair\nOpcão: '))

            if aux == 1:
                nome = input('Nome: ')
                mat = input('Matricula: ')
                np1 = input('NP1: ')
                np2 = input('NP2: ')

                aluno = {
                    'nome': nome,
                    'mat': mat,
                    'np1': np1,
                    'np2': np2
                }

                tcrud.create(aluno)
                print('\n')
                print('Aluno cadastrado')

            elif aux == 2:
                print('Alunos cadastrados na disciplina: \n')
                tcrud.read()


    elif (op == 1):
        while aux != 4:
            aux = int(input(f'Bem vindo aluno de Banco de Dados'
            f'Menu aluno:'
            f'1 - Ver nota da NP1'
            f'2 - Ver nota da NP2'
            f'3 - Ver nota final'
            f'4 - Sair\nOpcão: '))

            if aux == 1:
                break
            if aux == 2:
                break
            if aux == 3:
                break
            if aux == 4:
                break



