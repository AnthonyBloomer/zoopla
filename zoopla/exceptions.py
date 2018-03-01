class RequestFormatException(Exception):
    pass


class ResponseFormatException(Exception):
    pass


class ZooplaAPIException(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return "Zoopla returned an error: %s" % self.text
