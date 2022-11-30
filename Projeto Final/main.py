
from src.repository import Neo4J, AlunoRepository
from src.ui import CLI


def main() -> None:
    """"""

    uri = 'bolt://54.166.33.76:7687'
    user = 'neo4j'
    password = 'cycles-facepiece-baby'

    banco_neo4j = Neo4J(uri, user, password)

    aluno_repository = AlunoRepository(banco_neo4j)

    print("\n")
    user_interface = CLI(aluno_repository)
    user_interface.run()

    banco_neo4j.close()

    # elif (op == 1):
    #     while aux != 4:
    #         aux = int(input(f'Bem vindo aluno de Banco de Dados'
    #         f'Menu aluno:'
    #         f'1 - Ver nota da NP1'
    #         f'2 - Ver nota da NP2'
    #         f'3 - Ver nota final'
    #         f'0 - Sair\nOpcão: '))

    #         if aux == 1:
    #             mat1 = input('Digite sua matricula: \n')

    #             print('nota da NP1: \n')
    #             tcrud.readnp1(mat1)
    #         if aux == 2:
    #             mat2 = input('Digite sua matricula: \n')

    #             print('nota da NP2: \n')
    #             tcrud.readnp2(mat2)
    #         if aux == 3:
    #             mat3 = input('Digite sua matricula: \n')

    #             print('nota da NP2: \n')
    #             tcrud.notafinal(mat3)
    #         if aux == 0:
    #             break


if __name__ == '__main__':
    main()
