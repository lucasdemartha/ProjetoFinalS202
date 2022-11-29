from db.database import Graph

db = Graph(uri='bolt://54.166.33.76:7687', user='neo4j', password='cycles-facepiece-baby')

class crudmenu(object):

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