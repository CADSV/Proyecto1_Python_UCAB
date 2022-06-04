# Importaciones de librerias necesarias
import os #Para trabajar con el sistema operativo de la computadora desde la cual se esta ejecutando el programa
import sys

# Funcion encargada de mostrar todos los menus de la aplicacion
def create_menu(menu_options: list[str], title: str):
    print("\n")
    print(f'            {title}')
    for i in range(20):
        print("**", end="")
    print("\n")
    for i in range(len(menu_options)):
        print(f"  {i+1}. {menu_options[i]}")
    print("\n\n")

# Funcion encargada de limpiar la pantalla
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear") #Para limpiar la pantalla tanto en windows como en linux