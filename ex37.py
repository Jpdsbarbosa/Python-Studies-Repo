def salario(salario_atual, aumento_salario):
    """
    Função para demostrar salário com aumento

    """
    if isinstance(salario_atual, str) or isinstance(aumento_salario, str) or salario_atual == 0:
        print("Valores informados, Incorretos!")
    else:
        print(f"Salário inicial: R${salario_atual}\nSalário com aumento de {aumento_salario}: R$ {salario_atual * (1 + aumento_salario/100)}")

salario(1000, 12.87)
salario(1000, '10')
salario('1000', 10)
salario(0, 10)
