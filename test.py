import os
from tp1 import calcular_intersecciones

TEST_DIR = "tests"
SOSPECHOSO = 1
TRANSFERENCIA_CON_ERROR = 0
TRANSFERENCIA = 0
ERROR = 1

script_dir = os.path.dirname(__file__)
def get_test_files():
    target_dir = os.path.join(script_dir, TEST_DIR)
    files = os.listdir(target_dir)
    test_files = []
    for file in files:
        if file.endswith(".txt"):
            test_files.append(file)
    return test_files

def get_test_info(test_file):
    transferencias_sospechosas = []
    transferencias_sospechoso = []
    debe_ser_culpable = "no-es" not in test_file
    with open(os.path.join(script_dir, TEST_DIR, test_file), "r") as file:
        file.readline()
        n = int(file.readline().strip())
        for _ in range(n):
            transferencia = file.readline().strip().split(',')
            transferencia[0] = int(transferencia[0])
            transferencia[1] = int(transferencia[1])
            transferencias_sospechosas.append(transferencia)
        
        for _ in range(n):
            transferencia = int(file.readline().strip())
            transferencias_sospechoso.append(transferencia)
    
    return transferencias_sospechosas, transferencias_sospechoso, debe_ser_culpable

def test_tp1():
    test_files = get_test_files()
    for test_file in test_files:
        transferencias_sospechosas, transferencias_sospechoso, debe_ser_culpable = get_test_info(test_file)
        intersecciones, es_culpable = calcular_intersecciones(transferencias_sospechosas, transferencias_sospechoso)
        print(test_file)
        if es_culpable != debe_ser_culpable:
            print(f"Test failed: {test_file}, Expected: {"Culpable" if debe_ser_culpable else "No culpable"}, Got: {"Culpable" if es_culpable else "No Culpable"}")
            return
        
        if not es_culpable:
            print("No es el sospechoso correcto\n")
            continue

        for interseccion in intersecciones:
            print(f"{interseccion[SOSPECHOSO]} --> {interseccion[TRANSFERENCIA_CON_ERROR][TRANSFERENCIA]} ± {interseccion[TRANSFERENCIA_CON_ERROR][ERROR]}")
        print()

test_tp1()