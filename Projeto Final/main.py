
from src.repository import Neo4J, AlunoRepository
from src.ui import CLI


def main() -> None:
    """"""

    uri = 'bolt://44.203.4.43:7687'
    user = 'neo4j'
    password = 'injuries-crafts-maximum'

    banco_neo4j = Neo4J(uri, user, password)

    aluno_repository = AlunoRepository(banco_neo4j)

    print("\n")
    user_interface = CLI(aluno_repository)
    user_interface.run()

    banco_neo4j.close()


if __name__ == '__main__':
    main()
