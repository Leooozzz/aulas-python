class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

class Carrinho:
    def __init__(self):
        self.itens = []
        self.cupom = None

    def adicionar(self, produto, quantidade):
        if produto.estoque >= quantidade:
            self.itens.append((produto, quantidade))
            produto.estoque -= quantidade
        else:
            print(f"Estoque insuficiente de {produto.nome}")

    def remover(self, produto):
        self.itens = [item for item in self.itens if item[0] != produto]

    def aplicar_cupom(self, tipo, valor):
        self.cupom = (tipo, valor)  

    def totalizar(self):
        total = sum(prod.preco * qtd for prod, qtd in self.itens)
        if self.cupom:
            tipo, valor = self.cupom
            if tipo == "porcentagem":
                total *= (1 - valor / 100)
            elif tipo == "fixo":
                total -= valor
                total = max(total, 0)
        return total

class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.carrinho = Carrinho()

p1 = Produto("Camisa", 100, 10)
p2 = Produto("Calça", 150, 5)

cliente = Cliente("João", "Rua A, 123")


cliente.carrinho.adicionar(p1, 2)  
cliente.carrinho.adicionar(p2, 1)  

cliente.carrinho.aplicar_cupom("porcentagem", 10)

print(f"Total a pagar: R${cliente.carrinho.totalizar():.2f}")