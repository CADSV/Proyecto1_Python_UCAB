from exceptions.load_file_exceptions import EmptyFile, InvalidData #Excepciones de lectura
import time #Para trabajar con el tiempo en la barra de cargado

#Funcion obtenida en StackOverflow, que ayuda a determinar si un archivo es de texto plano o no
def is_text_plain_file(filepath: str) -> bool:
    """
    Check if the file is a text plain file.
    see: https://stackoverflow.com/a/7392391/19043850
    Params:
        filename (str): The path of the file.
    Returns:
        bool: True if the file is a text plain file, False otherwise.
    """

    textchars = bytearray(
        {7, 8, 9, 10, 12, 13, 27} |
        set(range(0x20, 0x100)) - {0x7f}
    )
    def is_binary_string(bytes): return bool(bytes.translate(None, textchars))
    return not is_binary_string(open(filepath, 'rb').read(1024))


#Funcion para validar el archivo a leer
def validate_file(file) -> bool:
    if (file.read() == ""):
        raise EmptyFile("¡ERROR! El archivo está vacío, no hay nada que leer :(")

    file.seek(0,0) #Como se leyó el archivo, se vuelve a poner al inicio el puntero

    # Se verifica que el archivo tenga los 10 campos que indica el ejercicio
    if (len(list(filter(lambda line: line.count(",") != 9, file.readlines()))) != 0):
        raise InvalidData("¡ERROR! Los participantes no cuentan con todo los datos necesarios :(")
   
    file.seek(0,0) #Como se leyó el archivo, se vuelve a poner al inicio el puntero

    return True

#Funcion para mostrar una barra de cargado
def load_bar(percent:int=0, width:int=40):
    left = width * percent // 100 #Para calcular la cantidad de asteriscos a mostrar
    right = width - left #Para calcular la cantidad de espacios en blanco a mostrar
    #Imprimiendo la barra con los valores calculados arriba
    print('\r\t[', '*' * left, ' ' * right, ']', f' {percent:.0f}%', sep='', end='', flush=True) 