# Importaciones de librerias necesarias
import os #Para trabajar con el sistema operativo
import sys

# Funcion encargada de mostrar todos los menus de la aplicacion
def create_menu(menu_options: list[str], title: str) -> dict:
    print("\n")
    print(title)
    for i in range(30):
        print("**", end="")
    print("\n")
    for i in range(len(menu_options)):
        print(f"  {i+1}. {menu_options[i]}")
    print("\n\n")