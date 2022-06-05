# Importaciones de librerias necesarias
import os #Para trabajar con el sistema operativo de la computadora desde la cual se esta ejecutando el programa
import sys

# Funcion encargada de mostrar todos los menus de la aplicacion
def create_menu(menu_options: list[str], title: str):
    print('\n')
    print(f'{title}') #Imprimimos el titulo del menu

    for i in range(20): #Imprimimos una linea de separacion
        print('**', end='')
    print('\n')

    for i in range(len(menu_options)): #Imprimimos las opciones del menu
        print(f'  {i+1}- {menu_options[i]}') #Imprimimos la opcion con su numero correspondiente
    print('\n\n')

# Funcion encargada de limpiar la pantalla
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') #Para limpiar la pantalla tanto en windows como en linux


# Funcion para despedirse del usuario y salir del sistema
def exit_system():
    clear_screen()
    print('\n')
    print('Espero que haya sido de su agrado, y no olvide armar su cubo rubik. Hasta pronto :)')
    print('\n')
    input('Por favor presione cualquier tecla para salir...')
    sys.exit()