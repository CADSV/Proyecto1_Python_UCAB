from exceptions.load_file_exceptions import (
    NotATextFile, #Excepcion de archivo no de texto
)

from data.utils import is_text_plain_file #Para validar si es o no un archivo de texto
from views.utils import clear_screen #Para limpiar la pantalla

# Funcion encargada de leer el archivo de texto
def load_txt_file(context: dict, isCustom: bool) -> dict:

    try:
        clear_screen()
        # Seleccionar el archivo a cargar
        if (isCustom):
            print('El archivo a cargar debe estar en la misma dirección que el archivo de ejecución main\n')
            file_name = input("Por favor ingrese el nombre del archivo a cargar: ")
        else:
            file_name = "competencia.txt"
        
        # Verificamos que el archivo sea de texto
        if not is_text_plain_file(file_name): #Si no lo es, lanza la excepcion
            raise NotATextFile("\n ¡ERROR! El archivo debe ser de Texto obligatoriamente :(")

        # Abrir el archivo
        file = open(file_name, "r")

        # Leer el archivo
    
    except NotATextFile as e:
        print(f'\n\n{e}\n')
        input("Por favor presione cualquier tecla para continuar...")

    
    else:
        print("\nExitos\n")
        input("Por favor presione cualquier tecla para continuar...")



    return context