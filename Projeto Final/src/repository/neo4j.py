
from typing import Any, Optional

from neo4j import GraphDatabase
from neo4j import Driver

# db = Graph(uri='bolt://54.166.33.76:7687', user='neo4j', password='cycles-facepiece-baby')


class Neo4J:
    _connection: Driver

    def __init__(self, uri: str, user: str, password: str) -> None:
        self._connection = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._connection.close()

    def execute_query(self, query: str, parameters: Optional[tuple[Any, ...]]=None) -> Optional[tuple[Any]]:
        data = []

        with self.driver.session() as session:
            results = session.run(query, parameters)

            for record in results:
                data.append(record)

            return data
