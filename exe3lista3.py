from datetime import datetime, timedelta

class Paciente:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

class Medico:
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade

class Consulta:
    def __init__(self, data, paciente, medico):
        self.data = data
        self.paciente = paciente
        self.medico = medico

class Agenda:
    def __init__(self):
        self.consultas = []

    def adicionar_consulta(self, consulta):
        if not self.tem_conflito(consulta):
            self.consultas.append(consulta)
            print(f"Consulta marcada: {consulta.paciente.nome} com {consulta.medico.nome} em {consulta.data}")
        else:
            print("Horário ocupado!")

    def tem_conflito(self, nova_consulta):
        for c in self.consultas:
            if c.medico == nova_consulta.medico and c.data == nova_consulta.data:
                return True
        return False

    def consulta_mais_proxima(self):
        if not self.consultas:
            return None
        return min(self.consultas, key=lambda c: c.data)

    def reagendar_consulta_mais_proxima(self):
        consulta = self.consulta_mais_proxima()
        if consulta is None:
            print("Nenhuma consulta para reagendar.")
            return

        nova_data = consulta.data + timedelta(hours=1)
        while self.tem_conflito(Consulta(nova_data, consulta.paciente, consulta.medico)):
            nova_data += timedelta(hours=1)

        print(f"Reagendando consulta de {consulta.paciente.nome} para {nova_data}")
        self.consultas.remove(consulta)
        self.consultas.append(Consulta(nova_data, consulta.paciente, consulta.medico))



p = Paciente("Maria", "111.111.111-11", "99999-0000")
m = Medico("Dr. José", "Dermatologia")

agenda = Agenda()

agenda.adicionar_consulta(Consulta(datetime(2025, 5, 20, 10), p, m))
agenda.adicionar_consulta(Consulta(datetime(2025, 5, 20, 11), p, m))


agenda.reagendar_consulta_mais_proxima()