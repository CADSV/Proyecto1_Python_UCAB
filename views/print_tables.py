#Funcion encargada de imprimir la tabla de todos los participantes
from views.utils import clear_screen #Para limpiar la pantalla


def list_all_participants(context: dict) -> dict:
    
    clear_screen()

    participants = context['participants'] #Se obtiene toda la data de los participantes

    print('\n\t{:100}'.format('LISTA DE TODOS LOS PARTICIPANTES'.center(100))) #Titulo de la tabla
    print('\n\t---------------------------------------------------------------------------------------------------------')
    
    #Encabezado de la tabla, con todo centrado
    print ('\t|{:3}|{:10}|{:16}|{:12}|{:16}|{:16}|{:6}|{:6}|{:10}|'.format('#'.center(3),'Cédula'.center(10),'Primer Nombre'.center(16),'2do Nombre'.center(12), 
                                                                    'Primer Apellido'.center(16),'Segundo Apellido'.center(16) , 'Sexo'.center(6), 
                                                                    'Edad'.center(6), 'Tiempo'.center(10)))
    print('\t---------------------------------------------------------------------------------------------------------')
    
    #Contenido de la tabla, con todo centrado
    for i, participant in enumerate(participants): #Para mostrar participante por participante
        print('\t|{:3}|{:10}|{:16}|{:12}|{:16}|{:16}|{:6}|{:6}|{:10}|'.format(str(i+1).center(3),str(participant['id']).center(10), str(participant['name']).center(16), str(participant['initial_name_letter']).center(12),
        str(participant['first_last_name']).center(16), str(participant['second_last_name']).center(16), str(participant['sex']).center(6), str(participant['age']).center(6), str(participant['total_time'].strftime('%H:%M:%S')).center(10)))
    print('\t---------------------------------------------------------------------------------------------------------\n\t', end='')


    return context