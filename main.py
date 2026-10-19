lista_prod = {
    1: {
        "id" : 1,
        "nome" : "Caderno",
        "preco_cent" : 1500,
        "qntd" : 10
    } ,
    2: {
        "id" : 2,
        "nome" : "Caneta",
        "preco_cent" : 500,
        "qntd" : 20
    } ,
    3: {
        "id" : 3,
        "nome" : "Lápis",
        "preco_cent" : 300,
        "qntd" : 15
    }
}

lista_promo = {
    1: {
        "descricao": "Combo escolar",
        "requisitos": {
            1: 6,   # 6 cadernos
            2: 48   # 48 lápis
        },
        "desconto": 0.3
    },
    2: {
        "descricao": "Combo de escrita",
        "requisitos": {
            2: 2,   # 2 lápis
            3: 2    # 2 canetas
        },
        "desconto": 0.1
    }
}

carrinho = {}

def retorna_qntd(id):
    return lista_prod[id]["qntd"]

def retorna_nome(id):
    return lista_prod[id]["nome"]

def retorna_preco(id):
    return lista_prod[id]["preco_cent"]

def adicionar_carrinho(id, qntd):
    if id in carrinho:
        carrinho[id]["qntd"] += qntd
    else:
        carrinho[id] = {
            "id" : id,
            "qntd" : qntd
        }

def checkout(carrinho, lista_prod):
    if not carrinho:
        return False
    for id, item in carrinho.items():
        if id not in lista_prod:
            print(f"Produto com ID {id} não encontrado na lista de produtos.")
            return False
        quantidade = item["qntd"]
        produto = lista_prod[id]

        if quantidade <= 0:
            print("Quantidade inválida.")
            return False
        if quantidade > produto["qntd"]:
            print(f"Estoque insuficiente para o produto {produto["nome"]}")
            return False
    return True


def verifica_promocao(carrinho, requisitos):
    for id_produto, quantidade_minima in requisitos.items():
        if id_produto not in carrinho:
            return False

        if carrinho[id_produto]["qntd"] < quantidade_minima:
            return False

    return True

def finalizar_compra(carrinho, lista_prod, lista_promo):
    if checkout(carrinho, lista_prod) != True:
        return False
    total = 0
    for id, item in carrinho.items():
        if verifica_promocao(carrinho, lista_promo[1]["requisitos"]):
            print(f"Promoção aplicada: {lista_promo[1]['descricao']}")
            total += (item["qntd"] * retorna_preco(id)) * lista_promo[1]["desconto"]
        elif verifica_promocao(carrinho, lista_promo[2]["requisitos"]):
            print(f"Promoção aplicada: {lista_promo[2]['descricao']}")
            total += (item["qntd"] * retorna_preco(id)) * lista_promo[2]["desconto"]