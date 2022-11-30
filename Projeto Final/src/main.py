from crud import crudmenu


def main() -> None:
    """"""
    tcrud = crudmenu()

    op = 0

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

            elif aux == 3:
                mat = input('Digite a matricula do aluno: ')

                tcrud.delete(mat)

                print('\n')
                print('Aluno deletado!')

            elif aux == 4:
                auxnp1 = input('Digite a nova nota da NP1: ')
                
                tcrud.updatenp1(auxnp1)
                
                print('\n')
                print('Nota atualizada!')
            
            elif aux == 5:
                auxnp2 = input('Digite a nova nota da NP2: ')
                
                tcrud.updatenp1(auxnp2)
                
                print('\n')
                print('Nota atualizada!')

            elif aux == 0:
                break


    elif (op == 1):
        while aux != 4:
            aux = int(input(f'Bem vindo aluno de Banco de Dados'
            f'Menu aluno:'
            f'1 - Ver nota da NP1'
            f'2 - Ver nota da NP2'
            f'3 - Ver nota final'
            f'0 - Sair\nOpcão: '))

            if aux == 1:
                mat1 = input('Digite sua matricula: \n')

                print('nota da NP1: \n')
                tcrud.readnp1(mat1)
            if aux == 2:
                mat2 = input('Digite sua matricula: \n')

                print('nota da NP2: \n')
                tcrud.readnp2(mat2)
            if aux == 3:
                mat3 = input('Digite sua matricula: \n')

                print('nota da NP2: \n')
                tcrud.notafinal(mat3)
            if aux == 0:
                break


if __name__ == '__main__':
    main()
