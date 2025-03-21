from typing import Optional
import json
import sqlite3


class SQLDB:
    def __init__(self):
        self.candidate_db_path = 'candidate_data.db'


class CandidateDB:
    def __init__(self, db_path: str):
        """
        Initialize the connection to the SQLite database.

        :param db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self.conn = None

    def connect(self) -> None:
        """
        Connect to the SQLite database.
        """
        self.conn = sqlite3.connect(self.db_path)

    def close(self) -> None:
        """
        Close the SQLite database connection.
        """
        if self.conn:
            self.conn.close()

    def simple_query(self, key: str, table: str, column: Optional[str]) -> dict:
        """
        Fetches the data from the 'candidates' table based on the provided key.

        :param key: The key to filter the candidate data.
        :return: A dictionary with the candidate data parsed from JSON.
        """
        if not self.conn:
            raise UserWarning("Database connection is not established. Call connect() first.")

        cursor = self.conn.cursor()
        query = f"""
            SELECT {column if column else '*'}
            FROM {table}
            WHERE key = ?
        """
        cursor.execute(query, (key,))
        idx = 0 if column else 1
        return json.loads(cursor.fetchone()[idx])
