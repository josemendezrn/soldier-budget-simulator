# Juego de soldados y monedas. Administración de presupuesto para Comprar Soldados
import random as r

# Definimos la funcion que genera soldados a peticion del usuario
def generar_soldado(identificar):
    tipo_solado = ["Arquero", "Francotirador", "Espadachín", "pistolero"]

    # RANDOM
    tipo_asignado = r.choice(tipo_solado)
    coste_asignado = r.randint(15, 60) # Rango costo de monedas

    return{
        'id': identificar,
        'tipo': tipo_asignado,
        'costo': coste_asignado
    }

# Le solicitaremos al usuario un conjunto de monedas a su elección
while True:
    monedas = input("Introduce la cantidad de monedas que posees para entrenar soldados: ")
    # Aprueba de balas para la cantidad de monedas
    try:
        monedas = int(monedas)
        break

    except ValueError:
        print('ERROR. Introduce un número entero.\n')


# Solicitamos la cantidad de soldados que se quieren entrenar
while True:
    cantidad_soldados = input("Introduce la cantidad de soldados que quieres entrenar: ")
    # Aprueba de balas para la cantidad de monedas
    try:
        cantidad_soldados = int(cantidad_soldados)
        break

    except ValueError:
        print('ERROR. Introduce un número entero.\n')


# Compra de soldados
peloton = []

for i in range(1, cantidad_soldados + 1):
    # llamamos la función y le asigmanos el # de orden como parámetro para el ID
    soldado_nuevo = generar_soldado(i)

    # Condicionales para realizar la compra-venta
    if soldado_nuevo['costo'] <= monedas:
        monedas -= soldado_nuevo['costo']
        peloton.append(soldado_nuevo)
        print(f"\nEl soldado {i}, un {soldado_nuevo['tipo']}, ha sido entrenado. Te queda(n) {monedas} moneda(s).\n")
    else:
        print('ERROR - No tienes suficientes monedas')
        print('Vuelve cuando tengas más monedas\n')
        break

# Muestreo final de al cantidad de soldados entrenada.
print(f"Acabas de entrenar a {len(peloton)} soldado(s). El Huesaso.")
