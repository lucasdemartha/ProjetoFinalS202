# from pprintpp import pprint as pp
from db.database import Graph
from helper.write_a_json import write_a_json as wj

db = Graph(uri='bolt://54.166.33.76:7687', user='neo4j', password='cycles-facepiece-baby')

if __name__ == '__main__':

 class CRUD(object):

    def __init__(self):
        self.db = db

    def create(self, aluno):
        return self.db.execute_query('create (a:Aluno{nome: $nome, mat: $mat, np1: $np1, np2: $np2}) RETURN a',
                                     {'nome': aluno['nome'], 'mat': aluno['matricula', 'np1': aluno['np1'], 'np2': aluno['np2']]})

    def read(self):
        return self.db.execute_query('match(n:Aluno) RETURN n.nome')

    def delete(self, aux):
        return self.db.execute_query('match (n:Aluno{mat: $mat}) DELETE n',
                                     {'mat': aux['matricula']})

    def updatenp1(self, aux, nota):
        return self.db.execute_query('match (n:Aluno{mat: $mat}) SET n.np1 = $np1 RETURN n',
                                     {'mat': aux, 'np1': nota})
    
    def updatenp2(self, aux, nota):
        return self.db.execute_query('match (n:Aluno{mat: $mat}) SET n.np2 = $np2 RETURN n',
                                     {'mat': aux, 'np2': nota})

    def readnp1(self,aux):
        return self.db.execute_query('match (n:Aluno{mat: $mat} RETURN n.np1',
                                     {'mat': aux})

    def readnp2(self,aux):
        return self.db.execute_query('match (n:Aluno{mat: $mat} RETURN n.np2',
                                     {'mat': aux})


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
            f'4 - deletar aluno'
            f'6 - atualizar nota da NP1'
            f'8 - atualizar nota da NP2'
            f'0 - Sair\nOpcão: '))

    if(op == 1):
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



