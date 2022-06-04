#Importaciones de librerias necesarias
import time #Para trabajar con el tiempo

#Funcion encargada de leer la data del archivo
def get_file_data(context: dict, file_name: str) -> dict:

    with open(file_name,'r') as file:
        #Aqui se le hace a cada participante un elemento de la lista de participantes, con toda su correspondiente data
        context['participants'] = list([
        {'id': data[0], 'first_last_name': data[1], 'second_last_name': data[2], 'name': data[3], 'initial_name_letter': data[4], 
        'sex': data[5], 'age': int(data[6]), 'time': time(hour=int(data[7]), minute=int(data[8]), second=int(data[9]))}
        for data in [line.split(',') for line in file.readlines()]])

        context['participants'].sort(key=lambda participant: participant['time']) #Organizamos de una vez a los participantes por tiempo

        #Funciones para extraer los grupos de datos especificos
        context = get_juniors(context)
        context = get_seniors(context)
        context = get_masters(context)
        context = get_participants_by_sex(context)

    
    return context


#Funcion que devuelve a los participantes juniors, ya organizados por tiempo
def get_juniors(context: dict) -> dict:

    ## Lista de participantes junior y organizamos la lista por el tiempo 
    context['juniors'] = list(filter(lambda participant: participant['age'] <= 25, context['participants']))
    context['juniors'].sort(key=lambda participant: participant['time'])

    context = get_juniors_by_sex(context)

    return context


#Funcion que devuelve a los participantes juniors, divididos por sexos
def get_juniors_by_sex(context: dict) -> dict:

    context['men_juniors'] = list(filter(lambda participant: participant['sex'].upper() == 'M', context['juniors'] ))
    context['women_juniors'] = list(filter(lambda participant: participant['sex'].upper() == 'F', context['juniors'] ))

    return context


#Funcion que devuelve a los participantes seniors, ya organizados por tiempo
def get_seniors(context: dict) -> dict:

    context['seniors'] = list(filter(lambda participant: participant['age'] > 25 and participant['age'] <= 40, context['participants']))
    context['seniors'].sort(key=lambda participant: participant['time'])

    context = get_seniors_by_sex(context)

    return context


#Funcion que devuelve a los participantes seniors, divididos por sexos
def get_seniors_by_sex(context: dict)-> dict:

    context['men_seniors'] = list(filter(lambda participant: participant['sex'].upper() == 'M', context['seniors'] ))
    context['women_seniors'] = list(filter(lambda participant: participant['sex'].upper() == 'F', context['seniors'] ))

    return context



#Funcion que devuelve a los participantes masters, ya organizados por tiempo
def get_masters(context: dict)-> dict:

    context['masters'] = list(filter(lambda participant: participant['age'] > 40, context['participants']))
    context['masters'].sort(key=lambda participant: participant['time'])

    context = get_masters_by_sex(context)

    return context


#Funcion que devuelve a los participantes masters, divididos por sexos
def get_masters_by_sex(context: dict) -> dict:

    context['men_masters'] = list(filter(lambda participant: participant['sex'].upper() == 'M', context['masters'] ))
    context['women_masters'] = list(filter(lambda participant: participant['sex'].upper() == 'F', context['masters'] ))

    return context


#Funcion que devuelve a los participantes masculinos y femeninos, ya organizados por 
def get_participants_by_sex(context: dict)-> dict:

    context['men'] = list(filter(lambda participant: participant['sex'] == 'M', context['participants']))
    context['men'].sort(key=lambda participant: participant['time'])

    context['women'] = list(filter(lambda participant: participant['sex'] == 'F', context['participants']))
    context['women'].sort(key=lambda participant: participant['time'])

    return context
