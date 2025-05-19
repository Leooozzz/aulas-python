from datetime import date

class Tarefa:
    def __init__(self, titulo, descricao, prioridade, status, vencimento):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade  
        self.status = status  
        self.vencimento = vencimento  

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

class GerenciadorDeTarefas:
    def __init__(self, usuario):
        self.usuario = usuario

    def ordenar_por_prioridade(self):
        return sorted(self.usuario.tarefas, key=lambda t: t.prioridade)

    def filtrar_por_status(self, status):
        return [t for t in self.usuario.tarefas if t.status == status]

    def lembretes_hoje(self):
        hoje = date.today()
        return [t for t in self.usuario.tarefas if t.vencimento == hoje and t.status == "pendente"]

u = Usuario("Maria")

t1 = Tarefa("Estudar", "Estudar Python", 1, "pendente", date.today())
t2 = Tarefa("Ir ao mercado", "Comprar frutas", 2, "pendente", date.today())
t3 = Tarefa("Lavar carro", "Antes do final de semana", 3, "concluída", date.today())

u.adicionar_tarefa(t1)
u.adicionar_tarefa(t2)
u.adicionar_tarefa(t3)

g = GerenciadorDeTarefas(u)

print("🔔 Lembretes para hoje:")
for t in g.lembretes_hoje():
    print(f"- {t.titulo} (Prioridade {t.prioridade})")