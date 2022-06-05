#Importaciones de librerias necesarias
from views.utils import clear_screen #Para limpiar la pantalla

#Funcion encargada de imprimir el total de participantes obtenidos
def total_participants_amount(context: dict) -> dict:

    clear_screen()

    participants = context['participants'] #Se obtiene toda la data de los participantes

    print('\n\t{:100}'.format('CANTIDAD TOTAL DE PARTICIPANTES'.center(100))) #Titulo de la accion
    print('\n\t---------------------------------------------------------------------------------------------------------')
    print('\n\t{:100}'.format(('La cantidad total de participantes es de -->  ' + str(len(participants)) + ' participantes' ).center(100))) #Cantidad total de participantes

    return context


#Funcion encargada de imprimir la cantiddad de participantes por sexo
def participants_by_gender_amount(context: dict) -> dict:

    clear_screen()

    men = context['men'] #Se obtiene la data correspondiente a los hombres
    women = context['women'] #Se obtiene la data correspondiente a las mujeres

    print('\n\t{:100}'.format('CANTIDAD TOTAL DE PARTICIPANTES POR SEXO'.center(100))) #Titulo de la accion
    print('\n\t---------------------------------------------------------------------------------------------------------')
    #Cantidad total de participantes por sexo
    print('\n\t{:100}'.format(('La cantidad total de participantes es de ' + str(len(women)) + ' mujeres y ' + str(len(men)) + ' hombres.' ).center(100))) 

    return context