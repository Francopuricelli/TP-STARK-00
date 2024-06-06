from data_stark import *
from os import system
def lista_campo(lista,campo):
    lista_retorno = []
    for el in lista:
        lista_retorno.append((el[campo]))
    return lista_retorno

#2
def filtrar_superheroes(lista, nombre,altura):
    lista_retorno = []
    for el in lista:
        if el["nombre"] == nombre:
            lista_retorno.append(el)
            if el["altura"] == altura:
                lista_retorno.append(el)
    return lista_retorno

def lista_nombre_altura(lista,nombre,altura):
    lista_retorno = []
    for el in lista:
        lista_retorno.append((el[nombre]))
        lista_retorno.append((el[altura]))
    return lista_retorno

def calcular_mayor_campo(lista,campo):
    if len(lista) == 0: 
        raise ValueError("no esta definido el mayor de una lista vacia")
    maximo = lista[0]
    for diccionarios in lista:
        if float(diccionarios[campo]) > float(maximo[campo]):
            maximo = diccionarios
            
    return maximo

def calcular_menor_campo(lista,campo)->float:
    if len(lista) == 0: 
        raise ValueError("no esta definido el mayor de una lista vacia")
    maximo = lista[0]
    for diccionarios in lista:
        if float(diccionarios[campo]) < float((maximo[campo])):
            maximo = diccionarios
            
    return maximo


def filtrar_superheroes(lista,altura):
    lista_retorno = []
    for el in lista:
        if el["altura"] == altura:
            lista_retorno.append(el)
    return lista_retorno

def promediar_lista(lista):
    total = 0
    for i in lista:
        total += i
    return total / i

def totalizar_lista(lista):
    total = 0
    for i in lista:
        total += i
    
    return total    


def promediar_coleccion(lista,campo): 
    """saca el promedio de una coleccion

    Args:
        lista (_type_): ingresa lista a promediar
        campo (_type_): ingresa campo a promediar

    Returns:
        _type_: devuelve el promedio del campo establecido en float
    """
    suma = 0
    total_iteraciones = len(lista)
    for personaje in lista:
        suma += float(personaje[campo])
        

    return suma / total_iteraciones


def promediar_coleccion_masc(lista,campo): 
    """saca el promedio de una coleccion

    Args:
        lista (_type_): ingresa lista a promediar
        campo (_type_): ingresa campo a promediar

    Returns:
        _type_: devuelve el promedio del campo establecido en float
    """
    suma = 0
    contador_masculino = 0
    for personaje in lista:
        if personaje["genero"] == "M":
            contador_masculino += 1
            suma += float(personaje[campo])
        

    return suma / contador_masculino

def promediar_coleccion_fem(lista,campo): 
    """saca el promedio de una coleccion

    Args:
        lista (_type_): ingresa lista a promediar
        campo (_type_): ingresa campo a promediar

    Returns:
        _type_: devuelve el promedio del campo establecido en float
    """
    suma = 0
    contador_fem = 0
    for personaje in lista:
        if personaje["genero"] == "F":
            contador_fem += 1
            suma += float(personaje[campo])
        

    return suma / contador_fem

def calcular_mayor_campo_nombre(lista,campo,campo2):
    """Le asigna un valor al campo 1

    Args:
        lista (_type_): ingresa lista 
        campo (_type_): campo a comparar
        campo2 (_type_): valor a asociar al campo

    Raises:
        ValueError: _description_

    Returns:
        _type_: el nombre asociado al campo a comparar
    """
    if len(lista) == 0: 
        raise ValueError("no esta definido el mayor de una lista vacia")
    nombre_maximo = lista[0]
    maximo = lista[0]
    for diccionarios in lista:
        if float(diccionarios[campo]) >= float(maximo[campo]):
            maximo = diccionarios
            nombre_maximo = diccionarios[campo2]
        
    return nombre_maximo

def calcular_menor_campo_nombre(lista,campo,campo2):
    if len(lista) == 0: 
        raise ValueError("no esta definido el mayor de una lista vacia")
    nombre_minimo = lista[0]
    minimo = lista[0]
    for diccionarios in lista:
        if float(diccionarios[campo]) <= float(minimo[campo]):
            minimo = diccionarios
            nombre_minimo = diccionarios[campo2]
        
    return nombre_minimo


def separador():
    print("-------------------------------------------------------------")

'''
def mapear_lista(funcion,lista): #  GENERICA
    for i in range (len(lista)):
        lista[i] = (funcion(lista[i]))
'''

#      FUNCIONES GENERICAS (LAMBDA)

def mapear_lista(funcion,lista):
    lista_retorno = []
    for el in lista:
        lista_retorno.append(funcion(el))
    return lista_retorno


def filtrar_lista(funcion,lista): # GENERICA
    lista_retorno = []
    for el in lista:
        if funcion(el):
            lista_retorno.append(el)
    return lista_retorno

def each_lista(funcion,lista): #  GENERICA
    for el in lista:
        funcion(el)

def reduce_lista(funcion, lista:list)->any :
    ant = lista[0]
    for el in lista[1:]:
        ant = funcion(ant, el)
    return ant


def calcular_mayor_campo_fem(lista,campo):
    if len(lista) == 0: 
        raise ValueError("no esta definido el mayor de una lista vacia")
    maximo = lista[0]
    for diccionarios in lista:
        if diccionarios["genero"] == "F":
            if float(diccionarios[campo]) > float(maximo[campo]):
                maximo = diccionarios
            
    return maximo


def calcular_menor_campo_fem(lista,campo):
    if len(lista) == 0: 
        raise ValueError("no esta definido el mayor de una lista vacia")
    minimo = lista[0]
    for diccionarios in lista:
        if diccionarios["genero"] == "F":
            if float(diccionarios[campo]) < float(minimo[campo]):
                minimo = diccionarios
            
    return minimo

def calcular_mayor_campo_masc(lista,campo):
    if len(lista) == 0: 
        raise ValueError("no esta definido el mayor de una lista vacia")
    maximo = lista[0]
    for diccionarios in lista:
        if diccionarios["genero"] == "M":
            if float(diccionarios[campo]) > float(maximo[campo]):
                maximo = diccionarios
            
    return maximo

def calcular_menor_campo_masc(lista,campo):
    if len(lista) == 0: 
        raise ValueError("no esta definido el mayor de una lista vacia")
    minimo = lista[0]
    for diccionarios in lista:
        if diccionarios["genero"] == "M":
            if float(diccionarios[campo]) < float(minimo[campo]):
                minimo = diccionarios
            
    return minimo



def nombre_max(lista,campo,campo2): #para masculinos
    """Le asigna un valor al campo 1

    Args:
        lista (_type_): ingresa lista 
        campo (_type_): campo a comparar
        campo2 (_type_): valor a asociar al campo

    Raises:
        ValueError: _description_

    Returns:
        _type_: el nombre asociado al campo a comparar
    """
    if len(lista) == 0: 
        raise ValueError("no esta definido el mayor de una lista vacia")
    nombre_maximo = lista[0]
    maximo = lista[0]
    for diccionarios in lista:
        if diccionarios["genero"] == "M":
            if float(diccionarios[campo]) >= float(maximo[campo]):
                maximo = diccionarios
                nombre_maximo = diccionarios[campo2]
        
    return nombre_maximo


def nombre_max1(lista,campo,campo2): #para femeninos
    """Le asigna un valor al campo 1

    Args:
        lista (_type_): ingresa lista 
        campo (_type_): campo a comparar
        campo2 (_type_): valor a asociar al campo

    Raises:
        ValueError: _description_

    Returns:
        _type_: el nombre asociado al campo a comparar
    """
    if len(lista) == 0: 
        raise ValueError("no esta definido el mayor de una lista vacia")
    nombre_maximo = lista[0]
    maximo = lista[0]
    for diccionarios in lista:
        if diccionarios["genero"] == "F":
            if float(diccionarios[campo]) >= float(maximo[campo]):
                maximo = diccionarios
                nombre_maximo = diccionarios[campo2]
        
    return nombre_maximo


def totalizar_lista(lista,campo):
    total = 0
    for diccionarios in lista:
        total += diccionarios[campo]
    
    return total    

def contador_lista(lista,campo):
    campo = {}
    for el in lista:
        campo[el] = 0

    for el in lista:
        for i in campo:
            if el == i:
                campo[el] += 1

    return campo

def enlistar(lista,campo1,campo_agrupado):
    #mapear lista previamente
    campo = {}
    for el in lista:
        campo[el] = ""

    for i in lista_personajes: #la lista cambia en base a la data
        for j in campo.keys():
            if i[campo1] == j:
                campo[j] += f"{i[campo_agrupado]} , "

    return campo


#######################################################################################

#                                              STARK 00
def nombre_superheroe():
    nombre_personajes = mapear_lista(lambda nombre : nombre["nombre"], lista_personajes)
    print(f"NOMBRES SUPERHEROES: \n {nombre_personajes}")
    separador()

def nombre_y_altura_superheroe():
    nombre_altura_personajes = mapear_lista(lambda nombre_altura : (nombre_altura["nombre"],nombre_altura["altura"]),lista_personajes)
    print(f"NOMBRE y ALTURA DEL SUPERHEROE: \n {nombre_altura_personajes}")
    separador()

def superheroe_mas_alto():
    superheroe_mas_alto = calcular_mayor_campo(lista_personajes,"altura")
    print(f"LA MAYOR ALTURA ES: \n {float(superheroe_mas_alto["altura"]):.2f}")
    separador()

def superheroe_mas_bajo():
    superheroe_mas_bajo = calcular_menor_campo(lista_personajes,"altura")

    print(f"LA MENOR ALTURA ES: \n {float(superheroe_mas_bajo["altura"]):.2f}")
    separador()

def promedio_altura():
    promedio_superheroes = promediar_coleccion(lista_personajes,"altura")
    print(f"LA ALTURA PROMEDIO DE LOS SUPERHEROES ES: \n {promedio_superheroes:.2f}")   
    separador()

def superheroe_altura_maximo_minimo():
    nombre_maximo = calcular_mayor_campo_nombre(lista_personajes,"altura","nombre")
    nombre_minimo = calcular_menor_campo_nombre(lista_personajes,"altura","nombre")
    print(f"el nombre del superheroe con mayor altura es: \n {nombre_maximo}")
    print(f"el nombre del superheroe con menor altura es: \n {nombre_minimo}")
    separador()

def superheroe_peso_maximo_minimo():
    superheroe_mas_liviano = calcular_menor_campo(lista_personajes,"peso") 
    superheroe_mas_pesado = calcular_mayor_campo(lista_personajes,"peso")
    print(f"EL MENOR PESO ES: \n {float(superheroe_mas_liviano["peso"]):.2f}")
    print(f"EL MAYOR PESO ES: \n {float(superheroe_mas_pesado["peso"]):.2f}")
    separador()

def salir():
    salir = input("desea salir? \n (si/no) ")
    return salir

def limpiar_pantalla():
    system("cls")

def pausar():
    system("pause")

def menu_heros_data():
    print("----------------Menu de opciones:  ")
    print("1- Mostrar lista de nombres de los héroes ")
    print("2- Mostrar lista de nombres y altura de los héroes ")
    print("3- Mayor/Menor altura de los héroes ")
    print("4- Promedio de alturas de los héroes ")
    print("5- Mostar nombre del héroe más/menos alto ")
    print("6- Mostrar nombre y peso del héroe más/menos pesado ")
    print("7- Mostrar nombre de los superheroes ")
    print("8- Mostrar nombre de las superheroinas ")
    print("9- Mostrar el superheroe mas alto ")
    print("10- Mostrar la superheroina mas alta ")
    print("11- Mostrar el superheroe mas bajo ")
    print("12- Mostrar la superheroina mas baja ")
    print("13- Mostrar el promedio de altura de los superheroes ")
    print("14- Mostrar el promedio de altura de las superheroinas ")
    print("15- Mostrar el superheroe mas alto y la superheroina mas alta ")
    print("16- Mostrar la lista del color de ojos ")
    print("17- Mostrar la lista del color de pelo ")
    print("18- Mostrar la lista de inteligencia ")
    print("19- Mostrar lista de superheroes basada en su color de ojos")
    print("20- Mostrar lista de superheroes basada en su color de pelo")
    print("21- Mostrar lista de superheroes basada en su inteligencia")
    print("22- Salir")
    option = input("Ingrese una opción: ")
    return option


######################################################################################################                           
#                                                                                       STARK 01


def nombre_male_hero():
    nombre_genero_personajes_m = mapear_lista(lambda nombre : nombre["nombre"], filtrar_lista(lambda genero : genero["genero"] == "M",lista_personajes))

    print(f"NOMBRES DE LOS SUPERHEROES MASCULINOS: \n {nombre_genero_personajes_m}")
    separador()


def nombre_female_hero():
    nombre_genero_personajes_f =  mapear_lista(lambda nombre : nombre["nombre"], filtrar_lista(lambda genero : genero["genero"] == "F",lista_personajes))

    print(f"NOMBRES DE LOS SUPERHEROES FEMENINOS: \n {nombre_genero_personajes_f}")
    separador()

def mas_alto_male():
    superheroe_mas_alto_M = calcular_mayor_campo_masc(lista_personajes,"altura")
    print(f"el nombre del superheroe masculino con mayor altura es: \n {superheroe_mas_alto_M} ")
    separador()

def mas_alto_female():
    superheroe_mas_alto_F = calcular_mayor_campo_fem(lista_personajes,"altura")
    print(f"el nombre del superheroe femenino con mayor altura es: \n {superheroe_mas_alto_F} ")
    separador()

def mas_bajo_male():
    super_mas_bajo = filtrar_lista(lambda hero : hero["genero"] == "M",lista_personajes)
    menor_altura_m= calcular_menor_campo(super_mas_bajo,"altura")
    print(f"el nombre del superheroe masculino con menor altura es: \n {menor_altura_m}")
    separador()

def mas_bajo_female():
    super_mas_bajo_f = filtrar_lista(lambda hero : hero["genero"] == "F",lista_personajes)
    menor_altura_f = calcular_menor_campo(super_mas_bajo_f,"altura")
    print(f"el nombre del superheroe femenino con menor altura es: \n {menor_altura_f}")
    separador()

def average_altura_male():
    superheroe_m_promedio = promediar_coleccion_masc(lista_personajes,"altura")

    print(f"LA ALTURA PROMEDIO DE LOS SUPERHEROES ES: \n {superheroe_m_promedio:.2f}")
    separador()

def average_altura_female():
    superheroe_f_promedio = promediar_coleccion_fem(lista_personajes,"altura")

    print(f"LA ALTURA PROMEDIO DE LAS SUPERHEROINAS ES: \n {superheroe_f_promedio:.2f}")
    separador()

def alto_nombre():
    nombre_masculino_mas_alto = nombre_max(lista_personajes,"altura","nombre")
    print(f"el nombre del superheroe masculino con mayor altura es: \n {nombre_masculino_mas_alto} ")

    nombre_femenino_mas_alto = nombre_max1(lista_personajes,"altura","nombre")
    print(f"el nombre del superheroe masculino con mayor altura es: \n {nombre_femenino_mas_alto} ")
    separador()


def lista_ojos_heros():
    color_ojos = contador_lista(mapear_lista(lambda hero : hero["color_ojos"],lista_personajes),"color_ojos")

    print(f"Lista color ojos: \n {color_ojos} ")
    separador() 

def lista_pelo_heros():
    color_pelo = contador_lista(mapear_lista(lambda hero : hero["color_pelo"],lista_personajes),"color_pelo")

    print(f"Lista color pelo: \n {color_pelo} ")
    separador()

def lista_inteligencia():
    inteligencia = contador_lista(mapear_lista(lambda hero : hero["inteligencia"],lista_personajes),"inteligencia")

    print(f"Lista inteligencia: \n {inteligencia} ")
    separador()

def listar_color_ojos():
    lista_por_color_ojos_mapeo = mapear_lista(lambda hero : hero["color_ojos"],lista_personajes)
    lista_por_color_ojos = enlistar(lista_por_color_ojos_mapeo,"color_ojos","nombre")

    print(f"Lista por color de ojos: \n  {lista_por_color_ojos}")
    separador()


def listar_color_pelo():
    lista_por_color_pelo_mapeo = mapear_lista(lambda hero : hero["color_pelo"],lista_personajes)
    lista_por_color_pelo = enlistar(lista_por_color_pelo_mapeo,"color_pelo","nombre")

    print(f"Lista por color de pelo: \n  {lista_por_color_pelo}")
    separador()

def listar_inteligencia():
    lista_por_inteligencia_mapeo = mapear_lista(lambda hero : hero["inteligencia"],lista_personajes)
    lista_por_inteligencia = enlistar(lista_por_inteligencia_mapeo,"inteligencia","nombre")

    print(f"Lista por inteligencia: \n  {lista_por_inteligencia}")