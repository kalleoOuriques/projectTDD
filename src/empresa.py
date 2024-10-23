from src.funcionario import Funcionario


class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def criar_funcionario(self, nome_funcionario):
        return Funcionario(nome_funcionario)

    def incluir_funcionario(self, funcionario):
        funcionario.id = len(self.funcionarios) + 1
        self.funcionarios.append(funcionario)