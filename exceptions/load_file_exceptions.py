# Excepcion de archivo no de texto
class NotATextFile(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message