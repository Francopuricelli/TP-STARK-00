from data_stark import *
from starkfunciones import *
from os import system
#B
nombre_personajes = mapear_lista(lambda nombre : nombre["nombre"], lista_personajes)
print(f"NOMBRES SUPERHEROES: \n {nombre_personajes}")
print("-----------------------------------------------------------------------")
#C
nombre_altura_personajes = mapear_lista(lambda nombre_altura : (nombre_altura["nombre"],nombre_altura["altura"]),lista_personajes)
print(f"NOMBRE y ALTURA DEL SUPERHEROE: \n {nombre_altura_personajes}")
print("-----------------------------------------------------------------------")
#D
superheroe_mas_alto = calcular_mayor_campo(lista_personajes,"altura")

print(f"LA MAYOR ALTURA ES: \n {float(superheroe_mas_alto["altura"]):.2f}")
print("-----------------------------------------------------------------------")
#E
superheroe_mas_bajo = calcular_menor_campo(lista_personajes,"altura")

print(f"LA MENOR ALTURA ES: \n {float(superheroe_mas_bajo["altura"]):.2f}")

#F 

promedio_superheroes = promediar_coleccion(lista_personajes,"altura")
print(f"LA ALTURA PROMEDIO DE LOS SUPERHEROES ES: \n {promedio_superheroes:.2f}")

#G

nombre_maximo = calcular_mayor_campo_nombre(lista_personajes,"altura","nombre")
print(f"el nombre del superheroe con mayor altura es: \n {nombre_maximo}")

nombre_minimo = calcular_menor_campo_nombre(lista_personajes,"altura","nombre")
print(f"el nombre del superheroe con menor altura es: \n {nombre_minimo}")

#H

superheroe_mas_liviano = calcular_menor_campo(lista_personajes,"peso")   
separador()
print(f"EL MENOR PESO ES: \n {float(superheroe_mas_liviano["peso"]):.2f}")
superheroe_mas_pesado = calcular_mayor_campo(lista_personajes,"peso")
print(f"EL MAYOR PESO ES: \n {float(superheroe_mas_pesado["peso"]):.2f}")


#J
while True:
    match menu_heros_data():
        case "1":
            nombre_superheroe()
        case "2":
            nombre_y_altura_superheroe()
        case "3":
            superheroe_mas_alto()
            superheroe_mas_bajo()
        case "4":
            promedio_altura()
        case "5":
            superheroe_altura_maximo_minimo()
        case "6":
            superheroe_peso_maximo_minimo()
        case "7":
            nombre_male_hero()
        case "8":
            nombre_female_hero()
        case "9":
            mas_alto_male()
        case "10":
            mas_alto_female()
        case "11":
            mas_bajo_male()
        case "12":
            mas_bajo_female()
        case "13":
            average_altura_male()
        case "14":
            average_altura_female()
        case "15":
            alto_nombre()
        case "16":
            lista_ojos_heros()
        case "17":
            lista_pelo_heros()
        case "18":
            lista_inteligencia()
        case "19":
            listar_color_ojos()
        case "20":
            listar_color_pelo()
        case "21":
            listar_inteligencia()
        case "22":
            if salir() == "no":
                menu_heros_data()
            else:
                break
        
    pausar()

print("Fin del programa")


