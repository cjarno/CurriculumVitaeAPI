import os
import datetime as dt
from deta import Deta
from typing import NoReturn, Optional
import json
import sqlite3
from ..Models import Message


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


# class DetaDB:
#     def __init__(self):
#         self.__deta = Deta(os.getenv("DETA_PROJECT_KEY"))
#         self.candidate_db = self.__deta.Base("Candidate")
#         self.message_db = self.__deta.Base("Messages")
#         self.admin_db = self.__deta.Base("Admin")
#         self._email = "cjarnold93@gmail.com"
#
#     def send_message(self, payload: Message, **kwargs) -> NoReturn:
#         """Send an email using the Deta Space preset."""
#         timestamp_str = dt.datetime.now().strftime("%Y%m%d%H%M%S%Z%f")
#         email_payload = dict(
#             to=self._email,
#             subject=f"CJA CV API | {payload.full_name} [{payload.company}]",
#             message=f"SENT AT {timestamp_str} || {self._format_payload(payload)}",
#             charset="UTF-8",
#         )
#         email_payload.update(*kwargs)
#         self.__deta.send_email(**email_payload)
#
#     @staticmethod
#     def _format_payload(payload) -> str:
#         return json.dumps(payload, indent=4, sort_keys=True, default=str)
