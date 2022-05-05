def convertKelvinInCelsius():

    temp = float(input("Temperatura in K: \n"))
    print(f"{temp}K in Celsius is: {temp - 273.15}°C" if temp >= 0 else "Don't exists temperature in K < 0")

convertKelvinInCelsius()
