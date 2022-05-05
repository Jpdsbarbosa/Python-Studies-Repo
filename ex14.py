from math import pi

def convertAnguloInRad():
    ang = float(input("Angulo em graus: "))
    print(f"{ang}° = {ang * pi/180} RAD")

convertAnguloInRad()
