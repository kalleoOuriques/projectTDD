from src.funcionario import Funcionario
from src.projeto import Projeto


class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.projetos = []

    def criar_funcionario(self, nome_funcionario):
        return Funcionario(nome_funcionario)

    def criar_projeto(self, nome_projeto):
        return Projeto(nome_projeto)

    def incluir_funcionario(self, funcionario):
        id_funcionario = len(self.funcionarios) + 1
        funcionario.id_funcionario = id_funcionario
        self.funcionarios.append(funcionario)
        return funcionario.id_funcionario

    def incluir_projeto(self, projeto):
        id_projeto = len(self.projetos) + 1
        projeto.id_projeto = id_projeto
        self.projetos.append(projeto)
        return projeto.id_projeto

    def obter_funcionario_por_id(self, id_funcionario):
        funcionario = self.funcionarios[id_funcionario - 1]
        return funcionario

    def obter_projeto_por_id(self, id_projeto):
        projeto = self.projetos[id_projeto - 1]
        return projeto

    def incluir_funcionario_em_projeto(self, funcionario, projeto):

        # Checar se funcionario ja estã na empresa
        for f in projeto.funcionarios:
            if funcionario.id_funcionario == f.id_funcionario:
                return 'Funcionario ja esta no projeto'

        projeto.funcionarios.append(funcionario)

        return 'Funcionario foi adicionado com sucesso'
