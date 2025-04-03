# CASOS EJEMPLO
# EJEMPLO_INTERVALOS_SOSPECHOSOS = [(10.34, 2.2), (5.33, 4), (8.12, 3.1), (7.45, 2.9), (19.2, 10), (10.4, 5)]
# EJEMPLO_TRANSFERENCIAS_DEL_SOSPECHOSO = [2, 5, 6, 8, 9, 10, 16]

# MACROS
TIEMPO,ERROR = 0,1

def esta_dentro_del_intervalo(intervalo, transferencia):
    """
    Función que devuelve un bool si la transferencia sospechosa está dentro del intervalo o no.
    Args:
        intervalo(tuple): Intervalo sospechoso con su tiempo y error.
        transferencia(float): Horario de la transferencia sospechosa.
    Returns:
        bool: Si la transferencia sospechosa está dentro del intervalo o no.
    """
    inicio, fin = intervalo[TIEMPO] - intervalo[ERROR],intervalo[TIEMPO] + intervalo[ERROR]
    return inicio <= transferencia <= fin


def calcular_intersecciones(intervalos_sospechosos, transferencias_del_sospechoso):
    """
    dado N Intervalos Sospechosos, devuelve los Intervalos en dónde coincide cada N Transferencia, junto con el booleano que define si el sospechoso es culpable o no.
    Args:
        intervalos_sospechosos(tuple): N Intervalos sospechosos con su tiempo y error.
        transferencias_del_sospechoso(float): Lista de N Transferencias Sospechosas (Su hora de ejecución).
    Returns:
        Devuelve:
            - intersecciones (tuple): Intervalos sospechosos juntos con sus respectivas transferencias coincidentes.
            - es_culpable (bool): Devuelve True si las N transferencias del sospechosas están dentro de los N intervalos.
    """
    intersecciones = []
    # Ordenar los intervalos de Menor a Mayor tiempo de finalización-
    intervalos_sospechosos.sort(key=lambda x: x[TIEMPO]+x[ERROR]) # O(n * log(n))
    
    for i in range(len(intervalos_sospechosos)):
        # En cada iteración, recorro uno a uno y compruebo si la transferencia (actual) está dentro del intervalo (actual).
        if esta_dentro_del_intervalo(intervalos_sospechosos[i], transferencias_del_sospechoso[i]):
            intersecciones.append((intervalos_sospechosos[i], transferencias_del_sospechoso[i]))

        # Sí la transferencia no está dentro del intervalo sospechoso actual, podría conicidir con uno posterior (Caso borde donde dos o más intervalos se superponen).
        # El algoritmo sigue siendo Greedy porque en cada iteración busca el óptimo local, y al encontrarlo, descarta esa posibilidad para futuras iteraciones.
        # En caso de no coincidir con algún próximo intervalo, el sospechoso no puede ser culpable, y por ende, dejamos de iterar.
        
        interseccion_con_intervalo_posterior = False
        for j in range(i, len(intervalos_sospechosos)): # Solo recorremos de la posición (i) actual en adelante
            if esta_dentro_del_intervalo(intervalos_sospechosos[j], transferencias_del_sospechoso[i]):
                # Intercambio el intervalo que me saltee (el anterior) con el usado (actual) -> Es 99% probable que la siguiente transferencia use ese intervalo.
                intervalos_sospechosos[i], intervalos_sospechosos[j] = intervalos_sospechosos[j], intervalos_sospechosos[i]
                intersecciones.append((intervalos_sospechosos[i], transferencias_del_sospechoso[i]))
                interseccion_con_intervalo_posterior = True
                break
        
        # Si no se encontro concordancia con ningun intervalo restante, el sospechoso NO puede ser culpable.
        if not interseccion_con_intervalo_posterior:
            return intersecciones, False

    # Retorno la culpabilidad del sospechoso con las N intersecciones.
    return intersecciones, True
