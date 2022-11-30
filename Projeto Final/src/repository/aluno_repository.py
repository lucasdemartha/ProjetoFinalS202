
from __future__ import annotations
from typing import TYPE_CHECKING, Any, Dict, List, Optional

if TYPE_CHECKING:
    from src.notas import Notas
    from src.repository import Neo4J


class AlunoRepository:
    repository: Neo4J

    def __init__(self, repository: Neo4J) -> None:
        """"""
        self.repository = repository

    def create(self, nome: str, matricula: str, notas: Notas) -> Optional[List[Dict[str, Any]]]:
        """"""
        query = 'CREATE (a:Aluno{nome: $nome, mat: $matricula, np1: $np1, np2: $np2, nota_final: $nota_final}) RETURN a;'

        values = {
            "nome": nome,
            "matricula": matricula,
            "np1": notas.np1,
            "np2": notas.np2,
            "nota_final": (notas.np1 + notas.np2) / 2
        }

        response = self.repository.execute_query(query, values)

        return response

    def read(self, matricula: str) -> Optional[List[Dict[str, Any]]]:
        """"""
        query = 'MATCH(a:Aluno{mat: $matricula}) RETURN a;'

        values = {"matricula": matricula}

        response = self.repository.execute_query(query, values)

        return response

    def read_all(self) -> Optional[List[Dict[str, Any]]]:
        """"""
        query = 'MATCH(a:Aluno) RETURN a;'

        response = self.repository.execute_query(query, None)

        return response

    def read_nota_final_average(self) -> Optional[float]:
        """"""
        query = 'MATCH(a:Aluno) RETURN AVG(a.nota_final);'

        response = self.repository.execute_query(query, None)

        if not response:
            return

        media_nota_final = response[0].get("AVG(a.nota_final)")

        return media_nota_final

    def read_np1(self, matricula: str) -> Optional[float]:
        query = 'MATCH(a:Aluno{mat: $matricula}) RETURN a.np1;'

        values = {"matricula": matricula}

        response = self.repository.execute_query(query, values)

        if not response:
            return

        return response[0].get('a.np1')

    def read_np2(self, matricula: str) -> Optional[float]:
        query = 'MATCH(a:Aluno{mat: $matricula}) RETURN a.np2;'

        values = {"matricula": matricula}

        response = self.repository.execute_query(query, values)

        if not response:
            return

        return response[0].get('a.np2')

    def read_nota_final(self, matricula: str) -> Optional[float]:
        query = 'MATCH(a:Aluno{mat: $matricula}) RETURN a.nota_final;'

        values = {"matricula": matricula}

        response = self.repository.execute_query(query, values)

        if not response:
            return

        return response[0].get('a.nota_final')

    def update(self, matricula: str, nova_matricula: str) -> Optional[List[Dict[str, Any]]]:
        """"""
        query = 'MATCH(a:Aluno{mat: $matricula}) SET a.mat = $nova_matricula RETURN a;'

        values = {
            "matricula": matricula,
            "nova_matricula": nova_matricula
        }

        response = self.repository.execute_query(query, values)

        return response

    def update_np1(self, matricula: str, np1: float) -> Optional[List[Dict[str, Any]]]:
        """"""
        query = 'MATCH(a:Aluno{mat: $matricula}) SET a.np1 = $np1 RETURN a;'

        values = {
            "matricula": matricula,
            "np1": np1
        }

        response = self.repository.execute_query(query, values)

        return response

    def update_np2(self, matricula: str, np2: float) -> Optional[List[Dict[str, Any]]]:
        """"""
        query = 'MATCH(a:Aluno{mat: $matricula}) SET a.np2 = $np2 RETURN a;'

        values = {
            "matricula": matricula,
            "np2": np2
        }

        response = self.repository.execute_query(query, values)

        return response

    def delete(self, matricula: str) -> None:
        """"""
        query = 'MATCH(a:Aluno{mat: $matricula}) DELETE a;'

        values = {"matricula": matricula}

        self.repository.execute_query(query, values)
