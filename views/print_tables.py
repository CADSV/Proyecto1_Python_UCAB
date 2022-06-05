#Funcion encargada de imprimir la tabla de todos los participantes
from views.utils import clear_screen #Para limpiar la pantalla


#Funcion encargada de imprimir la tabla de todos los participantes
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


#Funcion encargada de imprimir la cantiddad de participantes por grupo etario
def participants_by_age_group_amount(context: dict) -> dict:

    clear_screen()

    juniors = context['juniors'] #Se obtiene toda la data de los participantes juniors
    seniors = context['seniors'] #Se obtiene toda la data de los participantes seniors
    masters = context['masters'] #Se obtiene toda la data de los participantes masters

    print('\n\t{:45}'.format('CANTIDAD DE PARTICIPANTES POR GRUPO ETARIO'.center(45))) #Titulo de la tabla
    print('\n\t-----------------------------------------------')
    
    #Encabezado de la tabla, con todo centrado
    print ('\t|{:3}|{:14}|{:26}|'.format('#'.center(3),'Grupo Etario'.center(14),'Cantidad de Participantes'))
    print('\t-----------------------------------------------')
    
    #Contenido de la tabla, con todo centrado
    print('\t|{:3}|{:14}|{:26}|'.format('1'.center(3),'Juniors'.center(14), str(len(juniors)).center(26)))
    print('\t|{:3}|{:14}|{:26}|'.format('2'.center(3),'Seniors'.center(14), str(len(seniors)).center(26)))
    print('\t|{:3}|{:14}|{:26}|'.format('3'.center(3),'Masters'.center(14), str(len(masters)).center(26)))
    print('\t-----------------------------------------------\n\t', end='')

    return context