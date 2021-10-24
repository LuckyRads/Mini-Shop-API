from app.exceptions.exceptions import HttpException


class ValidationService:

    def check_validity(json, key_array):
        try:
            for key in key_array:
                if not json[key]:
                    raise HttpException(400, f'{key} is missing')
        except HttpException as e:
            raise e
        except Exception:
            raise HttpException(400, 'Invalid input')
