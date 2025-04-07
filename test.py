import os
from tp1 import *
import helpers

TEST_DIR = "tests"
SCRIPT_DIR = os.path.dirname(__file__)

def get_test_files():
    target_dir = os.path.join(SCRIPT_DIR, TEST_DIR)
    files = os.listdir(target_dir)
    test_files = []
    for file in files:
        if file.endswith(".txt"):
            test_files.append(file)
    return test_files

def test_tp1():
    test_files = get_test_files()
    for test_file in test_files:
        transferencias_sospechosas, transferencias_sospechoso = helpers.parse_file(F"{TEST_DIR}/{test_file}")
        debe_ser_culpable = "no-es" not in test_file
        intersecciones, es_culpable = calcular_intersecciones(transferencias_sospechosas, transferencias_sospechoso)
        
        helpers.print_results(test_file, intersecciones, es_culpable)
        if es_culpable != debe_ser_culpable:
            print(f"Test failed: {test_file}, Expected: {"Culpable" if debe_ser_culpable else "No culpable"}, Got: {"Culpable" if es_culpable else "No Culpable"}")
            return
        print()

test_tp1()