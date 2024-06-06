from data_stark import *
from starkfunciones import *
from os import system


#A

nombre_genero_personajes_m = mapear_lista(lambda nombre : nombre["nombre"], filtrar_lista(lambda genero : genero["genero"] == "M",lista_personajes))

print(f"NOMBRES DE LOS SUPERHEROES MASCULINOS: \n {nombre_genero_personajes_m}")
separador()

#B

nombre_genero_personajes_f =  mapear_lista(lambda nombre : nombre["nombre"], filtrar_lista(lambda genero : genero["genero"] == "F",lista_personajes))

print(f"NOMBRES DE LOS SUPERHEROES FEMENINOS: \n {nombre_genero_personajes_f}")
separador()

#C

superheroe_mas_alto_M = calcular_mayor_campo_masc(lista_personajes,"altura")
print(f"el superheroe masculino con mayor altura es: \n {superheroe_mas_alto_M} ")
separador()

#D

superheroe_mas_alto_F = calcular_mayor_campo_fem(lista_personajes,"altura")
print(f"el superheroe femenino con mayor altura es: \n {superheroe_mas_alto_F} ")
separador()

#E

super_mas_bajo = filtrar_lista(lambda hero : hero["genero"] == "M",lista_personajes)
menor_altura_m= calcular_menor_campo(super_mas_bajo,"altura")
print(f"el nombre del superheroe masculino con menor altura es: \n {menor_altura_m}")
separador()

#F
super_mas_bajo_f = filtrar_lista(lambda hero : hero["genero"] == "F",lista_personajes)
menor_altura_f = calcular_menor_campo(super_mas_bajo_f,"altura")
print(f"el nombre del superheroe femenino con menor altura es: \n {menor_altura_f}")
separador()


#G 

superheroe_m_promedio = promediar_coleccion_masc(lista_personajes,"altura")

print(f"LA ALTURA PROMEDIO DE LOS SUPERHEROES ES: \n {superheroe_m_promedio:.2f}")
separador()

#H

superheroe_f_promedio = promediar_coleccion_fem(lista_personajes,"altura")

print(f"LA ALTURA PROMEDIO DE LAS SUPERHEROINAS ES: \n {superheroe_f_promedio:.2f}")
separador()

#I
nombre_masculino_mas_alto = nombre_max(lista_personajes,"altura","nombre")
print(f"el nombre del superheroe masculino con mayor altura es: \n {nombre_masculino_mas_alto} ")

nombre_femenino_mas_alto = nombre_max1(lista_personajes,"altura","nombre")
print(f"el nombre del superheroe femenino con mayor altura es: \n {nombre_femenino_mas_alto} ")
separador()

#J


color_ojos = contador_lista(mapear_lista(lambda hero : hero["color_ojos"],lista_personajes),"color_ojos")

print(f"Lista color ojos: \n {color_ojos} ")
separador()

#K

color_pelo = contador_lista(mapear_lista(lambda hero : hero["color_pelo"],lista_personajes),"color_pelo")

print(f"Lista color pelo: \n {color_pelo} ")
separador()

#l

inteligencia = contador_lista(mapear_lista(lambda hero : hero["inteligencia"] if hero["inteligencia"] else "no tiene",lista_personajes),"inteligencia")

print(f"Lista inteligencia: \n {inteligencia} ")
separador()

#M
lista_por_color_ojos_mapeo = mapear_lista(lambda hero : hero["color_ojos"],lista_personajes)
lista_por_color_ojos = enlistar(lista_por_color_ojos_mapeo,"color_ojos","nombre")

print(f"Lista por color de ojos: \n  {lista_por_color_ojos}")
separador()

#N

lista_por_color_pelo_mapeo = mapear_lista(lambda hero : hero["color_pelo"],lista_personajes)
lista_por_color_pelo = enlistar(lista_por_color_pelo_mapeo,"color_pelo","nombre")

print(f"Lista por color de pelo: \n  {lista_por_color_pelo}")
separador()

#O

lista_por_inteligencia_mapeo = mapear_lista(lambda hero : hero["inteligencia"] ,lista_personajes)
lista_por_inteligencia = enlistar(lista_por_inteligencia_mapeo,"inteligencia","nombre")

print(f"Lista por inteligencia: \n  {lista_por_inteligencia}")
separador()