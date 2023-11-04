import requests
from requests import Response


class Telegram:
    """Connection to the Telegram Bot service."""

    def __init__(self, auth_key: str, group_id: str):
        self.__telegram_bot_auth = auth_key
        self.__telegram_group_id = group_id

    def send_message(self, payload: dict) -> Response:
        telegram_api_url = (f"https://api.telegram.org/bot{self.__telegram_bot_auth}"
                            f"/sendMessage?chat_id={self.__telegram_group_id}"
                            f"&parse_mode=MarkdownV2"
                            f"&text={self._format_payload(payload)}")
        telegram_response = requests.get(telegram_api_url)
        return telegram_response

    @staticmethod
    def _format_payload(payload) -> str:
        return f"""`full_name={payload.get('full_name')}`
            `email={payload.get('email')}`
            `mobile={payload.get('mobile')}`
            `company={payload.get('company')}`
            `timestamp={payload.get('timestamp')}`
            `message={payload.get('message')}`"""
