def entrada_num(texto):
    return int(input(texto))

def dashboard(entrada):
    entrada = entrada_num("\n===== Dashboard ====="
    "\n1 - Adicionar Produto!"
    "\n2 - Remover Produto!"
    "\n3 - Ver Carrinho!"
    "\n4 - Virar/Remover Cliente Fiel" 
    "\n5 - Finalizar Pedido"
    "\n0 - Cancelar Pedido\n\nDigite sua entrada: ")
    return entrada

def menu(lista):
    print("\n====== MENU =======")
    # O segredo está aqui: o enumerate separa o índice (i) do conteúdo (item)
    for i in range(len(lista)):
        nome = lista[i][0]    # Ou: nome = lista[i][0]
        preco = lista[i][1]   # Ou: preco = lista[i][1]
        print(f'{i} - {nome} (R${preco})')


def selecionar_produto(prod):
        if prod == 1:
            nome, valor = "X-Burger", 10
        elif prod == 2:
            nome, valor = "Batata Frita", 8
        elif prod == 3:
            nome, valor = "Refrigerante", 5
        elif prod == 4:
            nome, valor = "Milkshake", 12
        else:
            nome, valor = None, None
        return [nome, valor]

def adicionar_produto (selected, qntd):
    nome_prod = selected[0]
    valor = selected[1]*qntd
    texto = f"\nVocê adicionou {qntd} unidades do produto {selected[0]}."
    if qntd >= 4 and qntd < 12:
        valor = valor* 0.9
        print(texto + " Parabéns!! você ganhou o desconto familia!!!")
    elif qntd>=12:
        valor = valor* 0.75
        print(texto + " Parabéns!! você ganhou o desconto firma!!!")
    else:
        print(texto)
    return [nome_prod, valor, qntd]

def mostrar_carrinho(lista):
    if len(lista)<1:
        print("Você ainda não possui nenhum produto no carrinho!")
    else:
        print("\n=====SEU CARRINHO======")
        for i in range(len(lista)):
            nome = lista[i][0]
            valor = lista[i][1]
            qntd = lista[i][2]
            print(f"\n{i} - {qntd} unidades de {nome}, no valor de {valor:.2f}")

valor_total = 0
qntd_total = 0
lista_compras = []
lista_produtos = [["X-Burger", 10],["Batata Frita", 8],["Refrigerante", 5],["Milkshake", 12]]
fidelidade = False
print("Olá! Bem-vindo a lanchonete!!")
x=1

while True:
    dashboard = entrada_num("\n===== Dashboard ====="
    "\n1 - Adicionar Produto!"
    "\n2 - Remover Produto!"
    "\n3 - Ver Carrinho!"
    "\n4 - Virar/Remover Cliente Fiel" 
    "\n5 - Finalizar Pedido"
    "\n0 - Cancelar Pedido\n\nDigite sua entrada: ")

    if dashboard == 1:
        option = int(input("\n===== MENU ====="
        "\n1 - X-Burger (R$10)" 
        "\n2 - Batata (R$8)"
        "\n3 - Refrigerante (R$5)"
        "\n4 - Milkshake (R$12)\n\nDigite sua entrada: "))
        prod_selecionado = selecionar_produto(option)

        if prod_selecionado[0] == None:
            print("Erro na escolha")

        else:
            quantidade = entrada_num(f"\nQuantos {prod_selecionado[0]} deseja adicionar? ")
            add = adicionar_produto(prod_selecionado, quantidade)
            lista_compras.append(add)

    elif dashboard == 2:
        print("\nescolha um produto para remover:")
        mostrar_carrinho(lista_compras)
        entrada = entrada_num("\nEscolha um produto para remover: ")
        nome = lista_compras[entrada][0]
        valor = lista_compras[entrada][1]
        qntd = lista_compras[entrada][2]
        print(f"\nRemovendo: {entrada} - {qntd} unidades de {nome}, no valor de {valor:.2f}")
        del lista_compras[entrada]

    elif dashboard == 3:
        mostrar_carrinho(lista_compras)

    elif dashboard == 4:
        fidelidade = not fidelidade
        print("\n========FIDELIDADE=========")

        if fidelidade == True:
            print("\nParabéns!! agora você é Cliente Fiel!!")

        else:
            print("\nCliente Fiel removido!")

    elif dashboard == 5:
        total = 0
        mostrar_carrinho(lista_compras)
        print(lista_compras)
        for i in range(len(lista_compras)):
            valor_total += lista_compras[i][1]
            qntd_total += lista_compras[i][2]
        if fidelidade == True:
            valor_total = valor_total * 0.9
        print(f"\n======TOTAL======\nO total do pedido foi R${valor_total} com {qntd_total} produtos.")
        break

    elif dashboard == 0:
        print("\n\n PEDIDO CANCELADO!!!!")
        break

    else:
        print("\n\nErro!! Opção fora do dashboard!!")

print("Tenha um ótimo dia!!")