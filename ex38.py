def encanador_salario(valor_dia, dias):
    """
    função para definir o valor a ser pago para um encanador em função dos dias trabalhados, ja descontados impostos de 8%
    """
    imposto = 1 - 8/100

    if isinstance(valor_dia, str) or isinstance(dias, str) or valor_dia == 0:
        print("Dados informados incorretos")
    else:
        print(f"O encanador trabalhou {dias} dias\nRecebeu por dia: R${valor_dia}\nTotal recebido líquido: R$ {valor_dia*dias*imposto}")

encanador_salario(30, 10)
