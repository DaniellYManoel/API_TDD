def product_data():
    return {
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": "8.500",
        "status": True,
    }

# product_data: Essa função retorna um dicionário que representa os dados de um produto específico.
# name: O nome do produto (neste caso, "Iphone 14 Pro Max").
# quantity: A quantidade do produto em estoque (neste caso, 10 unidades).
# price: O preço do produto (neste caso, "8.500").
# status: O status do produto, indicando se está disponível ou não (neste caso, True, significando que está disponível).


def products_data():
    return [
        {"name": "Iphone 11 Pro Max", "quantity": 20, "price": "4.500", "status": True},
        {"name": "Iphone 12 Pro Max", "quantity": 15, "price": "5.500", "status": True},
        {"name": "Iphone 13 Pro Max", "quantity": 5, "price": "6.500", "status": True},
        {
            "name": "Iphone 15 Pro Max",
            "quantity": 3,
            "price": "10.500",
            "status": False,
        },
    ]


# products_data: Essa função retorna uma lista de dicionários, cada um representando os dados de diferentes produtos.
# Primeiro produto: "Iphone 11 Pro Max" com 20 unidades em estoque, preço "4.500" e disponível (status: True).
# Segundo produto: "Iphone 12 Pro Max" com 15 unidades em estoque, preço "5.500" e disponível (status: True).
# Terceiro produto: "Iphone 13 Pro Max" com 5 unidades em estoque, preço "6.500" e disponível (status: True).
# Quarto produto: "Iphone 15 Pro Max" com 3 unidades em estoque, preço "10.500" e não disponível (status: False).