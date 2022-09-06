
from enum import Enum


class StatusEnum(Enum):
    SUCCESS = 0
    FAILED = 1


class BasicResponse:
    status: StatusEnum
    message: str = ''

    def __init__(self, status: StatusEnum, message: str) -> None:
        self.status = status
        self.message = message

    @staticmethod
    def get_response(status: StatusEnum, message: str):
        return BasicResponse(status, message)

    @staticmethod
    def get_dict_res(status: StatusEnum, message: str) -> dict:
        return BasicResponse.get_response(status, message).to_dict()

    def to_dict(self) -> dict:
        return {'status': self.status.name, 'message': self.message}
