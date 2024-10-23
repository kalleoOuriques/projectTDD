from src.funcionario import Funcionario


class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def criar_funcionario(self, nome_funcionario):
        return Funcionario(nome_funcionario)

    def incluir_funcionario(self, funcionario):
        id_funcionario = len(self.funcionarios) + 1
        funcionario.id_funcionario = id_funcionario
        self.funcionarios.append(funcionario)
        return id