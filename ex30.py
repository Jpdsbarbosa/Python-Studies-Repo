def converteRealDolar():
    cotacao = float(input("Cotação Dolar: "))
    real = float(input("Quantidade de reais: "))
    print(f"R${real} == ${real / cotacao}")

converteRealDolar()