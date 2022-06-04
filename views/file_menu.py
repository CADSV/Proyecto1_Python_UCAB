# Importacions de librerias necesarias
from ast import Break
from views.utils import (
    create_menu, #Para crear el menu
    clear_screen, #Para limpiar la pantalla
    call_exit, #Para salir del programa
    )
from exceptions.menu_exceptions import InexistentMenuOptionError #Excepcion de opcion invalida en el menu


def file_menu(context: dict) -> dict:
    selected_option = None
    main_menu_options = ["Cargar un archivo", "Volver al Menú Principal", "Salir del Programa"]

    while(True):
        try: 
            clear_screen()

            create_menu(main_menu_options, "            MENÚ DE ARCHIVOS")

            selected_option = int(input("Por favor seleccione una opción: "))

            if (selected_option == 1):
                # file_menu(context)
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