from math import pi

def convertRadInGraus():
    ang = float(input("Angulo in RAD: "))
    print(f"{ang} RAD = {ang * 180 / pi}°")

convertRadInGraus()