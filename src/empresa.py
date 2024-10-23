from src.funcionario import Funcionario
from src.projeto import Projeto


class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def criar_funcionario(self, nome_funcionario):
        return Funcionario(nome_funcionario)

    def criar_projeto(self, nome_projeto):
        return Projeto(nome_projeto)

    def incluir_funcionario(self, funcionario):
        id_funcionario = len(self.funcionarios) + 1
        funcionario.id_funcionario = id_funcionario
        self.funcionarios.append(funcionario)
        return funcionario.id_funcionario