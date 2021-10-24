class HttpException(Exception):
    '''Exception raised for HTTP requests'''
    code: int = 0
    message: str = ''

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
        super().__init__(self.message)
