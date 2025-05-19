import matplotlib.pyplot as plt

class Transacao:
    def __init__(self, valor, tipo, data, categoria):
        self.valor = valor
        self.tipo = tipo
        self.data = data
        self.categoria = categoria

class Carteira:
    def __init__(self, saldo=0.0, transacoes=[]):
        self.saldo = saldo
        self.transacoes = transacoes

    def adicionar_transacao(self, valor, tipo, data, categoria):
        transacao = Transacao(valor, tipo, data, categoria)
        self.transacoes.append(transacao)
        self.saldo += valor
        print(f"Transação de {tipo} no valor de {valor} adicionada em {data}.")
        print(f"Novo saldo: {self.saldo:.2f}")

    def resumo_mensal(self):
        if not self.transacoes:
            print("Nenhuma transação registrada.")
            return

        print("\n--- Resumo de Transações ---")
        saida_por_categoria = {}
        for transacao in self.transacoes:
            print(f"Data: {transacao.data}, Tipo: {transacao.tipo}, Valor: {transacao.valor:.2f}, Categoria: {transacao.categoria}")
            if transacao.tipo == "saida":
                if transacao.categoria in saida_por_categoria:
                    saida_por_categoria[transacao.categoria] += abs(transacao.valor)
                else:
                    saida_por_categoria[transacao.categoria] = abs(transacao.valor)

        categorias = list(saida_por_categoria.keys())
        valores = list(saida_por_categoria.values())

        if categorias:
            plt.figure(figsize=(5, 8))
            plt.bar(categorias, valores, color='black')
            plt.xlabel("Categoria da saida")
            plt.ylabel("Valor Gasto")
            plt.title("Grafico de Gastos")
            plt.tight_layout()
            plt.show()
        else:
            print("Nenhuma saida registrada para gerar o gráfico.")

minha_carteira = Carteira()

minha_carteira.adicionar_transacao(3000.00, "entrada", "2025-05-19", "salário")
minha_carteira.adicionar_transacao(-250.00, "saida", "2025-05-19", "alimentação")
minha_carteira.adicionar_transacao(-50.00, "saida", "2025-05-20", "transporte")
minha_carteira.adicionar_transacao(50.00, "entrada", "2025-05-21", "renda extra")
minha_carteira.adicionar_transacao(-150.00, "saida", "2025-05-22", "lazer")

minha_carteira.resumo_mensal()

print(f"\nSaldo final da carteira: {minha_carteira.saldo:.2f}")