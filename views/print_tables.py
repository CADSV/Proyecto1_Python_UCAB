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
        print('\t---------------------------------------------------------------------------------------------------------')


    return context


#Funcion encargada de imprimir la cantiddad de participantes por grupo etario
def participants_by_age_group_amount(context: dict) -> dict:

    clear_screen()

    juniors = context['juniors'] #Se obtiene toda la data de los participantes juniors
    seniors = context['seniors'] #Se obtiene toda la data de los participantes seniors
    masters = context['masters'] #Se obtiene toda la data de los participantes masters

    options = {'Juniors': juniors, 'Seniors': seniors, 'Masters': masters} #Diccionario con los ganadores por grupo etario

    print('\n\t{:45}'.format('CANTIDAD DE PARTICIPANTES POR GRUPO ETARIO'.center(45))) #Titulo de la tabla
    print('\n\t-----------------------------------------------')
    
    #Encabezado de la tabla, con todo centrado
    print ('\t|{:3}|{:14}|{:26}|'.format('#'.center(3),'Grupo Etario'.center(14),'Cantidad de Participantes'))
    print('\t-----------------------------------------------')
    
    #Contenido de la tabla, con todo centrado
    for i in enumerate(options): #Para mostrar grupo por grupo
        print('\t|{:3}|{:14}|{:26}|'.format(str(i[0]+1).center(3),str(i[1]).center(14), str(len(options[i[1]])).center(26)))
        print('\t-----------------------------------------------')

    return context


#Funcion que imprime la tabla con los ganadores por grupo etario
def winners_by_age_group(context: dict) -> dict:

    clear_screen()
    
    junior = context['juniors'][0] #Se obtiene la data del participante junior ganador
    senior = context['seniors'][0] #Se obtiene la data del participante senior ganador
    master = context['masters'][0] #Se obtiene la data del participante master ganador

    options = {'Juniors': junior, 'Seniors': senior, 'Masters': master} #Diccionario con los ganadores por grupo etario

    print('\n\t{:85}'.format('GANADORES POR GRUPO ETARIO'.center(85))) #Titulo de la tabla
    print('\n\t------------------------------------------------------------------------------------------')
    
    #Encabezado de la tabla, con todo centrado
    print ('\t|{:3}|{:14}|{:10}|{:16}|{:16}|{:6}|{:6}|{:10}|'.format('#'.center(3),'Grupo Etario'.center(14),'Cédula'.center(10),
        'Primer Nombre'.center(16),'Primer Apellido'.center(16),'Sexo'.center(6),'Edad'.center(6), 'Tiempo'.center(10)))
    print('\t------------------------------------------------------------------------------------------')
    
    #Contenido de la tabla, con todo centrado
    for i in enumerate(options): #Para imprimir el resultado de cada diccionario
        print('\t|{:3}|{:14}|{:10}|{:16}|{:16}|{:6}|{:6}|{:10}|'.format(str(i[0]+1).center(3),str(i[1]).center(14), str(options[i[1]]['id']).center(10), 
            str(options[i[1]]['name']).center(16), str(options[i[1]]['first_last_name']).center(16), str(options[i[1]]['sex']).center(6), 
            str(options[i[1]]['age']).center(6), str(options[i[1]]['total_time'].strftime('%H:%M:%S')).center(10)))
        print('\t------------------------------------------------------------------------------------------')

    return context


#Funcion que imprime la tabla con los ganadores por edad
def winners_by_gender(context: dict) -> dict:

    clear_screen()
    
    men = context['men'][0] #Se obtiene la data del participante hombre ganador
    women = context['women'][0] #Se obtiene la data de la participante mujer ganadora

    options = {'Mujeres': women, 'Hombres': men} #Diccionario con los ganadores por sexo

    print('\n\t{:85}'.format('GANADORES POR SEXO'.center(85))) #Titulo de la tabla
    print('\n\t------------------------------------------------------------------------------------------')
    
    #Encabezado de la tabla, con todo centrado
    print ('\t|{:3}|{:14}|{:10}|{:16}|{:16}|{:6}|{:6}|{:10}|'.format('#'.center(3),'Grupo Etario'.center(14),'Cédula'.center(10),
        'Primer Nombre'.center(16),'Primer Apellido'.center(16),'Sexo'.center(6),'Edad'.center(6), 'Tiempo'.center(10)))
    print('\t------------------------------------------------------------------------------------------')
    
    #Contenido de la tabla, con todo centrado
    for i in enumerate(options): #Para imprimir el resultado de cada diccionario
        print('\t|{:3}|{:14}|{:10}|{:16}|{:16}|{:6}|{:6}|{:10}|'.format(str(i[0]+1).center(3),str(i[1]).center(14), str(options[i[1]]['id']).center(10), 
            str(options[i[1]]['name']).center(16), str(options[i[1]]['first_last_name']).center(16), str(options[i[1]]['sex']).center(6), 
            str(options[i[1]]['age']).center(6), str(options[i[1]]['total_time'].strftime('%H:%M:%S')).center(10)))
        print('\t------------------------------------------------------------------------------------------')

    return context


#Funcion que imprime un histograma de la cantidad de participantes por grupo etario
def histogram_by_age_group(context: dict) -> dict:

    clear_screen()

    juniors = context['juniors'] #Se obtiene toda la data de los participantes juniors
    seniors = context['seniors'] #Se obtiene toda la data de los participantes seniors
    masters = context['masters'] #Se obtiene toda la data de los participantes masters

    options = {'Juniors': juniors, 'Seniors': seniors, 'Masters': masters} #Diccionario con los ganadores por grupo etario

    print('\n{:120}'.format('HISTOGRAMA DE PARTICIPANTES POR GRUPO ETARIO\n'.center(120))) #Titulo de la tabla
    
    #Histograma de la cantidad de participantes por grupo etario
    for i in enumerate(options): #Para mostrar grupo por grupo
        print('{:7}({}):|{}'.format(str(i[1]), str(len(options[i[1]])), '*'*len(options[i[1]])))

    return context