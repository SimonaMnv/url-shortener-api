class ResponseCodeStatusException(Exception):
    def __init__(self, message=None):
        super().__init__(f'Response status Error 'f'{message}')


class BadURLException(Exception):
    def __init__(self, message):
        super().__init__(f'URL format is not valid: {message}')


class BadServiceName(Exception):
    def __init__(self, message):
        super().__init__(f'Provider name is not valid: {message}')
