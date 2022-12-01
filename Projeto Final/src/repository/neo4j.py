
from typing import Any, Dict, List, Optional

from neo4j import GraphDatabase
from neo4j import Driver


class Neo4J:
    _connection: Driver

    def __init__(self, uri: str, user: str, password: str) -> None:
        self._connection = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._connection.close()

    def execute_query(self, query: str, parameters: Optional[Dict[str, Any]]) -> Optional[List[Dict[str, Any]]]:
        data = []

        with self._connection.session() as session:
            results = session.run(query, parameters)

            for record in results:
                data.append(record)

            return data
