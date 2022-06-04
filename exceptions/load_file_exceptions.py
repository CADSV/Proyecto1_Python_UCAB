# Excepcion de archivo no de texto
class NotATextFile(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message

#Excepcion para lectura de data invalida
class InvalidData(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message

#Excepcion cuando un archivo leido esta vacio
class EmptyFile(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message