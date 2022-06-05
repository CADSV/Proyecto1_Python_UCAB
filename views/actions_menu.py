#Importaciones de librerias necesarias
from exceptions.menu_exceptions import InexistentMenuOptionError #Excepcion para opcion inexistente en el menu

from views.utils import (
    exit_system, #Para salir del programa
    clear_screen, #Para limpiar la pantalla
    create_menu, #Para crear el menu con sus opciones
)

from views.print_tables import (
    list_all_participants, #Funcion que imprime la lista de participantes
)

from views.print_one_lines import(
    total_participants_amount,
)



#Funcion encargada de mostrar el menu de acciones
def actions_menu(context: dict) -> dict:

    selected_option = None
    actions_menu_options = [
        'Lista con la totalidad de participantes',
        'Cantidad total de participantes',
        'Cantidad de participantes por grupo etario',
        'Cantidad de participantes por sexo',
        'Ganadores por grupo etario',
        'Ganadores por sexo',
        'Ganadores por grupo etario y sexo',
        'Ganador general',
        'Histograma de participane por grupo etario',
        'Promedio de tiempo por grupo etario y sexo',
        'Volver al Menú Principal',
        'Salir del Programa'
    ]

    if(context): #En caso de que el contexto no este vacio, es decir, que se haya leido el archivo y cargado su data
        
        while(True):
            try:
                clear_screen()

                create_menu(actions_menu_options, '            MENÚ DE ACCIONES') #Creamos el menu

                selected_option = int(input('Por favor seleccione una opción: '))

                if (selected_option == 1):
                    list_all_participants(context)
                
                elif (selected_option == 2):
                    total_participants_amount(context)
                
                # elif (selected_option == 3):
                #     participants_by_age_group_amount(context)

                # elif (selected_option == 4):
                #     participants_by_gender_amount(context)
                
                # elif (selected_option == 5):
                #     winners_by_age_group(context)
                
                # elif (selected_option == 6):
                #     winners_by_gender(context)

                # elif (selected_option == 7):

                elif (selected_option == 11):
                    break

                elif (selected_option == 12):
                    exit_system()

                else:
                    raise InexistentMenuOptionError('¡ERORR! La opción seleccionada no existe. Por favor seleccione una opción válida :(')

                input('\n\nPor favor presione cualquier tecla para continuar...') #Para poder visualizar con calma todas las opciones del menu
  
            except InexistentMenuOptionError as e:
                print(f'\n\n{e}\n')
                input('Por favor presione cualquier tecla para continuar...')

            except ValueError:
                print('\n\n¡ERROR! El valor ingresado no es valido, por favor intente nuevamente con un número entero :(\n')	
                input('Por favor presione cualquier tecla para continuar...')


    else: #En caso de que el contexto si este vacio, es decir, que no se haya leido el archivo
        clear_screen()
        print('\n¡ERROR! No se ha cargado ningun archivo, y por ende no puede ejecutar ninguna acción :(\n')
        input('Por favor presione cualquier tecla para continuar...')

    return context