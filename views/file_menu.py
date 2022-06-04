# Importacions de librerias necesarias
from views.utils import (
    create_menu, #Para crear el menu
    clear_screen #Para limpiar la pantalla
    )

def file_menu(context: dict) -> dict:
    context = None
    selected_option = None
    main_menu_options = ["Archivo", "Acciones", "Salir del Programa"]

    while(True):
        try: 
            clear_screen()

            print('\n')
            print('Bienvenidos al primer proyecto de Python')
            print('Desarrollado por: Calos Doffiny S-V.  CI: V-27.814.707')

            create_menu(main_menu_options, "MENÚ PRINCIPAL")

            selected_option = int(input("Por favor seleccione una opción: "))

            if (selected_option == 1):
                # file_menu(context)
                print('111')

            elif (selected_option == 2):
                # actions_menu(context)
                print('222')

            elif (selected_option == 3):
                # call_exit()
                print('333')
            else:
                raise InexistentMenuOptionError("¡ERORR! La opción seleccionada no existe. Por favor seleccione una opción válida :(")
        
        except ValueError:
            print("\n\n¡ERROR! El valor ingresado no es valido, por favor intente nuevamente con un número entero :(\n")	
            input("Por favor presione cualquier tecla para continuar...")
        
        except (InexistentMenuOptionError) as e:
            print(f'\n\n{e}\n')
            input("Por favor presione cualquier tecla para continuar...")

    return context