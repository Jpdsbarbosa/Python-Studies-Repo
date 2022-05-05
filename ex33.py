from math import pi

def areaCirculo(raio):
    raio = float(raio)
    print(f"Raio = {raio}cm\nÁrea do circulo = {2 * pi * raio**2}cm²")

areaCirculo(5)