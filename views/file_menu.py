# Importacions de librerias necesarias
from ast import Break
from views.utils import (
    create_menu, #Para crear el menu
    clear_screen, #Para limpiar la pantalla
    call_exit, #Para salir del programa
    )
from exceptions.menu_exceptions import InexistentMenuOptionError #Excepcion de opcion invalida en el menu
from data.load_txt_file import load_txt_file #Para cargar el archivo


# Funcion encargada de mostrar el menu de los archivos
def file_menu(context: dict) -> dict:
    selected_option = None
    main_menu_options = ["Cargar un archivo", "Volver al Menú Principal", "Salir del Programa"] #Lista de las opciones

    while(True):
        try: 
            clear_screen()

            create_menu(main_menu_options, "            MENÚ DE ARCHIVOS") #Creamos el menu

            selected_option = int(input("Por favor seleccione una opción: "))

            if (selected_option == 1):
                load_file_menu(context)
                print('111')

            elif (selected_option == 2):
                break

            elif (selected_option == 3):
                call_exit()
            else:
                raise InexistentMenuOptionError("¡ERORR! La opción seleccionada no existe. Por favor seleccione una opción válida :(")
        
        except ValueError:
            print("\n\n¡ERROR! El valor ingresado no es valido, por favor intente nuevamente con un número entero :(\n")	
            input("Por favor presione cualquier tecla para continuar...")
        
        except (InexistentMenuOptionError) as e:
            print(f'\n\n{e}\n')
            input("Por favor presione cualquier tecla para continuar...")

    return context


# Funcion encargada de mostrar el menu de cargar un archivo
def load_file_menu(context: dict) -> dict:
    selected_option = None
    main_menu_options = ["Cargar el archivo por defecto competencia.txt", "Cargar un archivo propio", "Volver al Menú de Archivos", "Salir del Programa"]

    while(True):
        try: 
            clear_screen()

            create_menu(main_menu_options, "         MENÚ DE CARGAR ARCHIVOS")

            selected_option = int(input("Por favor seleccione una opción: "))

            if (selected_option == 1):
                load_txt_file(context, False)

            elif (selected_option == 2):
                load_txt_file(context, True)

            elif (selected_option == 3):
                break

            elif (selected_option == 4):
                call_exit()
            else:
                raise InexistentMenuOptionError("¡ERORR! La opción seleccionada no existe. Por favor seleccione una opción válida :(")
        
        except ValueError:
            print("\n\n¡ERROR! El valor ingresado no es valido, por favor intente nuevamente con un número entero :(\n")	
            input("Por favor presione cualquier tecla para continuar...")
        
        except (InexistentMenuOptionError) as e:
            print(f'\n\n{e}\n')
            input("Por favor presione cualquier tecla para continuar...")

    return context