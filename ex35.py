from math import pi

def volumeCilindro(altura, raio):
    if type(altura) == str or type(raio) == str:
        print("Altura ou Raio informados não funcionam para o cálculo!")
    else:
        print(f"Volume do cilindro = {pi * raio**2 * altura} cm³")

volumeCilindro(5, 2.5)
volumeCilindro(5, '2.5')
