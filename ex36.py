def valorProdutoDesconto(valorProduto, descontoProduto):
    if type(valorProduto) == str or type(descontoProduto) == str or valorProduto == 0:
        print("Valores informador errados")
    else:
        print(f"Valor Produto: {valorProduto}\nValor Produto com desconto de {descontoProduto}%: R${valorProduto * (1 - descontoProduto/100)}")

valorProdutoDesconto(100, 30)

valorProdutoDesconto(100, '30')

valorProdutoDesconto(0, 30)