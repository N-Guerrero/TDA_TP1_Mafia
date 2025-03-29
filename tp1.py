# Timestamps de transferencias sospechosas
EJEMPLO_TRANSFERENCIAS_SOSPECHOSAS = [(10.34, 2.2), (5.33, 4), (8.12, 3.1), (7.45, 2.9), (19.2, 10), (10.4, 5)]

# Timestamps del sospechoso
EJEMPLO_TRANSFERENCIAS_DEL_SOSPECHOSO = [2, 5, 6, 8, 9, 10, 16]

def hay_interseccion(tranferencia_sospechosa, transferencia_del_sospechoso):
    inicio_transferencia_sospechosa = tranferencia_sospechosa[0] - tranferencia_sospechosa[1]
    fin_transferencia_sospechosa = tranferencia_sospechosa[0] + tranferencia_sospechosa[1]
    return inicio_transferencia_sospechosa <= transferencia_del_sospechoso and fin_transferencia_sospechosa >= transferencia_del_sospechoso


def calcular_intersecciones(transferencias_sospechosas, transferencias_del_sospechoso):
    intersecciones = []
    # Ordena por tiempo de inicio
    transferencias_sospechosas.sort(key=lambda x: x[0]-x[1]) # O(n * log(n))
    for i in range(len(transferencias_sospechosas)):
        if not hay_interseccion(transferencias_sospechosas[i], transferencias_del_sospechoso[i]):
            # No es culpable
            return intersecciones, False
        intersecciones.append((transferencias_sospechosas[i], transferencias_del_sospechoso[i]))
    # Es culpable
    return intersecciones, True
