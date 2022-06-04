#Importaciones de librerias necesarias
from exceptions.load_file_exceptions import (
    EmptyFile, #Excepcion por si el archivo esta vacio
    NotATextFile, #Excepcion de archivo no de texto
    InvalidData, #Excepcion para lectura de data invalida
)

from data.utils import (
    is_text_plain_file, #Para validar si es o no un archivo de texto
    load_bar, #Para mostrar la barra de cargado
    validate_file #Para validar el archivo
) 
from views.utils import clear_screen #Para limpiar la pantalla

import time #Para trabajar con el tiempo

from controllers.functions import get_file_data #Funcion para cargar la data


# Funcion encargada de leer el archivo de texto
def load_txt_file(context: dict, isCustom: bool) -> dict:

    try:
        clear_screen()
        # Seleccionar el archivo a cargar
        if (isCustom):
            print('El archivo a cargar debe estar en la misma dirección que el archivo de ejecución main\n')
            file_name = input('Por favor ingrese el nombre del archivo a cargar: ')
        else:
            file_name = 'competencia.txt'
        
        # Verificamos que el archivo sea de texto
        if not is_text_plain_file(file_name): #Si no lo es, lanza la excepcion
            raise NotATextFile('\n ¡ERROR! El archivo debe ser de Texto obligatoriamente :(')

        # Abrir el archivo
        file = open(file_name, 'r')

        if(validate_file(file)):
            get_file_data(context, file) #Para obtener toda la data

          
    
    except (NotATextFile, InvalidData, EmptyFile) as e:
        print(f'\n\n{e}\n')
        input('Por favor presione cualquier tecla para continuar...')
    
    except FileNotFoundError:
        print('\n¡ERORR! Lo sentimos, el archivo no ha sido encontrado :(\n')
        input('Presione una tecla para continuar')
    
    except:
        print('\n¡ERORR! Lo sentimos, no se pudo leer el archivo :(\n')
        input('Por favor presione cualquier tecla para continuar...')

    
    else:
        clear_screen()
        print(f'\n            CARGANDO ARCHIVO {file_name.upper()}...\n', end='')
        for i in range(101):
            load_bar(i)
            time.sleep(0.01)
        print('')
        print(f'\n\n¡BIEN! El archivo {file_name} ha sido leido con éxito\n')
        input('Por favor presione cualquier tecla para continuar...')



    return context