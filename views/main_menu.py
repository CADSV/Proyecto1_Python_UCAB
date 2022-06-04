# Importacions de librerias necesarias
from views.utils import create_menu
# from views.utils import create_menu, clear_screen, call_exit
# from views.files import file_menu
# from views.actions import actions_menu

# Funcion encargada de mostrar el menu principal
def main(context: dict) -> dict:
    selected_option = None
    main_menu_options = ["Archivo", "Acciones", "Salir"]

    while(True):
        try: 
            # clear_screen()

            create_menu(main_menu_options, "Menu Principal")

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
                raise InexistentMenuOptionError("La opción seleccionada no existe")
        
        except ValueError:
            print("\nEl valor ingresado no es valido, por favor intente nuevamente con un número entero\n")	
            input("Por favor presione cualquier tecla para continuar...")
        
        except (InexistentMenuOptionError) as e:
            print(f'\n{e}\n')
            input("Por favor presione cualquier tecla para continuar...")
