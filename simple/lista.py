import numpy as np
from random import randint

if __name__ == "__main__":
        lista = []
        for idx in range(10):
                input_dict = {
                        "id": idx,
                        "edad": randint(1,100)
                }
                lista.append(input_dict)
        lista= sorted(lista, key=lambda d:d["edad"])
        print(lista)
        print(lista[0]["id"])
        print(lista[-1]["id"])