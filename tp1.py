# Timestamps de transferencias sospechosas
EJEMPLO_TIMESTAMPS_TRANSFERENCIAS_SOSPECHOSAS = [(10.34, 2.2), (5.33, 4), (8.12, 3.1), (7.45, 2.9), (19.2, 10), (10.4, 5)]

# Timestamps del sospechoso
EJEMPLO_TIMESTAMPS_SOSPECHOSO = [2, 5, 6, 8, 9, 10, 16]

def hay_interseccion(tranferencia_sospechosa, transferencia_del_sospechoso):
    inicio_transferencia_sospechosa = tranferencia_sospechosa[0] - tranferencia_sospechosa[1]
    fin_transferencia_sospechosa = tranferencia_sospechosa[0] + tranferencia_sospechosa[1]
    return inicio_transferencia_sospechosa <= transferencia_del_sospechoso and fin_transferencia_sospechosa >= transferencia_del_sospechoso


def calcular_intersecciones(timestamps_transferencias, timestamps_sospechoso):
    intersecciones = []
    # Ordena por tiempo de inicio
    timestamps_transferencias.sort(key=lambda x: x[0]-x[1]) # O(n * log(n))
    for i in range(len(timestamps_transferencias)):
        if not hay_interseccion(timestamps_transferencias[i], timestamps_sospechoso[i]):
            # No es culpable
            return intersecciones
        intersecciones.append((timestamps_transferencias[i], timestamps_sospechoso[i]))
    # Es culpable
    return intersecciones

def main():
    # O(n * log(n)) por ordenar los timestamps + O(n) por recorrerlos
    intersecciones = calcular_intersecciones(EJEMPLO_TIMESTAMPS_TRANSFERENCIAS_SOSPECHOSAS, EJEMPLO_TIMESTAMPS_SOSPECHOSO)
    sospechoso_es_culpable = len(intersecciones) == len(EJEMPLO_TIMESTAMPS_TRANSFERENCIAS_SOSPECHOSAS)
    
    for interseccion in intersecciones:
        print(f"Intervalo: {interseccion[0]}, Transferencia del sospechoso: {interseccion[1]}")
    print(f"El sospechoso {'es' if sospechoso_es_culpable else 'no es'} culpable.")

main()