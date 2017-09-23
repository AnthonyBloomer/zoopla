class RequestFormatException(Exception):
    pass


class ResponseFormatException(Exception):
    pass


class ZooplaAPIException(Exception):
    def __init__(self, status_code, reason, text):
        self.status_code = status_code
        self.reason = reason
        self.text = text

    def __str__(self):
        return "Zoopla returned an error: {code} - {reason} - {message}".format(
            code=self.status_code, reason=self.reason, message=self.text)
