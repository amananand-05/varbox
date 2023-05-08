class Exception(Exception):
    pass
class GenericException(Exception):
    def __init__(self, error_message = "unknown error"):
        super().__init__(error_message)



