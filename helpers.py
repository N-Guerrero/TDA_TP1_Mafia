import sys

TRANSFERENCIA_CON_ERROR, SOSPECHOSO = 0,1
TRANSFERENCIA, ERROR = 0,1

def parse_file(file_path):
    transferencias_sospechosas = []
    transferencias_sospechoso = []
    try:
        with open(file_path, "r") as file:
            first_line = file.readline()
            while first_line.startswith("#"):
                first_line = file.readline()
            n = int(first_line.strip())
            for _ in range(n):
                transferencia = file.readline().strip().split(',')
                transferencia[0] = int(transferencia[0])
                transferencia[1] = int(transferencia[1])
                transferencias_sospechosas.append(transferencia)
            
            for _ in range(n):
                transferencia = int(file.readline().strip())
                transferencias_sospechoso.append(transferencia)
        
        return transferencias_sospechosas, transferencias_sospechoso
    except:
        print(f"Error: No se pudo abrir el archivo en la ubicación {file_path}")
        sys.exit(1)

def print_results(file_path, intersecciones, es_culpable):
    # Nombre del archivo
    print(file_path.split("/")[-1])
    
    # Mensaje si no es culpable
    if not es_culpable:
        print("No es el sospechoso correcto")
        return
    
    # Match de transferencias si es culpable
    for interseccion in intersecciones:
        print(f"{interseccion[SOSPECHOSO]} --> {interseccion[TRANSFERENCIA_CON_ERROR][TRANSFERENCIA]} ± {interseccion[TRANSFERENCIA_CON_ERROR][ERROR]}")