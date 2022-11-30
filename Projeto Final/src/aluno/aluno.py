
from dataclasses import dataclass
from typing import Any, Optional

from src.notas import Notas
from src.repository import Neo4J


@dataclass
class Aluno:
    repository: Neo4J

    def create(self, nome: str, matricula: str, notas: Notas) -> Optional[tuple[Any]]:
        """"""
        query = 'CREATE (a:Aluno{nome: %s, mat: %s, np1: %s, np2: %s) RETURN a;'
        values = (nome, matricula, notas.np1, notas.np2)

        response = self.repository.execute_query(query, values)

        return response

    def read(self, matricula: str) -> Optional[tuple[Any]]:
        """"""
        query = 'MATCH(a:Aluno{mat: %s}) RETURN a;'
        values = (matricula,)

        response = self.repository.execute_query(query, values)

        return response

    def update(self, matricula: str, nova_matricula: str) -> Optional[tuple[Any]]:
        """"""
        query = 'MATCH(a:Aluno{mat: %s}) SET a.mat = %s RETURN a;'
        values = (matricula, nova_matricula)

        response = self.repository.execute_query(query, values)

        return response

    def delete(self, matricula: str):
        """"""
        query = 'MATCH(a:Aluno{mat: %s}) DELETE a;'
        values = (matricula,)

        response = self.repository.execute_query(query, values)

        return response

    def read_all(self) -> Optional[tuple[Any]]:
        """"""
        query = 'MATCH(a:Aluno) RETURN a;'

        response = self.repository.execute_query(query, None)

        return response
