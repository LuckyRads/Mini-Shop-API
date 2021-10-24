class BasicResponse:
    status: str = ''
    message: str = ''

    def __init__(self, status: str, message: str) -> None:
        self.status = status
        self.message = message
        return {'status': status, 'message': message}
