import os
import datetime as dt
from deta import Deta
from typing import NoReturn
import json
from ..Models import Message


class DetaDB:
    def __init__(self):
        self.__deta = Deta(os.getenv("DETA_PROJECT_KEY"))
        self.candidate_db = self.__deta.Base("Candidate")
        self.message_db = self.__deta.Base("Messages")
        self.admin_db = self.__deta.Base("Admin")
        self._email = "cjarnold93@gmail.com"

    def send_message(self, payload: Message, **kwargs) -> NoReturn:
        """Send an email using the Deta Space preset."""
        timestamp_str = dt.datetime.now().strftime("%Y%m%d%H%M%S%Z%f")
        email_payload = dict(
            to=self._email,
            subject=f"CJA CV API | {payload.full_name} [{payload.company}]",
            message=f"SENT AT {timestamp_str} || {self._format_payload(payload)}",
            charset="UTF-8",
        )
        email_payload.update(*kwargs)
        self.__deta.send_email(**email_payload)

    @staticmethod
    def _format_payload(payload) -> str:
        return json.dumps(payload, indent=4, sort_keys=True, default=str)
