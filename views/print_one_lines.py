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


#Funcion que imprime el ganador absoluto de la competencia
def absolute_winner(context: dict) -> dict:

    clear_screen()

    winner = context['participants'][0] #Se obtiene toda la data del ganador absoluto

    print('\n\t{:100}'.format('GANADOR ABSOLUTO DE LA COMPETENCIA'.center(100))) #Titulo de la accion
    print('\n\t---------------------------------------------------------------------------------------------------------')
    #Cantidad total de participantes por sexo
    print('\n\t{:100}'.format(('El Ganador absoluto de la competencia es ' + str(winner['name']).upper() + str(winner['first_last_name']).upper() + ' de ' 
        + str(winner['age']) + ' años, gracias a su tiempazo de ' + str(winner['total_time'].strftime('%H:%M:%S'))).center(100))) 

    return context
