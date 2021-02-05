class ResponseCodeStatusException(Exception):
    def __init__(self, message=None):
        super().__init__(f'Response status Error '
                         f'{message}')


# TODO: check with regex the url format
class BadURLException(Exception):
    def __init__(self, message):
        super().__init__(f'URL format is not valid: {message}')
