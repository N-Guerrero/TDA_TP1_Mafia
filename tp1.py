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
    # Ordena por tiempo de fin
    transferencias_sospechosas.sort(key=lambda x: x[0]+x[1]) # O(n * log(n))
    
    for i in range(len(transferencias_sospechosas)):
        # Si las transferencias coinciden, la agrego a la lista salto a la iteración siguiente
        if hay_interseccion(transferencias_sospechosas[i], transferencias_del_sospechoso[i]):
            intersecciones.append((transferencias_sospechosas[i], transferencias_del_sospechoso[i]))
            continue

        # Si la transferencia no coincide con la transferencia sospechosa actual, podría conicidir con una posterior (caso borde de transferencias solapadas donde una contiene a la otra).
        # El algoritmo sigue siendo Greedy porque en cada iterción busca el óptimo local, y al encontrarlo, descarta esa posibilidad para futuras iteraciones.
        # En caso de no encontrarlo el algoritmo termina, diciendo que el sospechoso no es culpable
        interseccion_con_transaccion_posterior = False
        for j in range(i, len(transferencias_sospechosas)):
            if hay_interseccion(transferencias_sospechosas[j], transferencias_del_sospechoso[i]):
                transferencias_sospechosas[i], transferencias_sospechosas[j] = transferencias_sospechosas[j], transferencias_sospechosas[i]
                intersecciones.append((transferencias_sospechosas[i], transferencias_del_sospechoso[i]))
                interseccion_con_transaccion_posterior = True
                break
        
        # Si no coincidió con ninguna de las restantes, el sospechoso no es el culpable
        if not interseccion_con_transaccion_posterior:
            return intersecciones, False

    # Es culpable
    return intersecciones, True
