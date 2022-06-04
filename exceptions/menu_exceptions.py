
#Excepcion de opcion inexistente en el menu
class InexistentMenuOptionError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

