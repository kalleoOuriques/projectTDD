from src.funcionario import Funcionario
from src.ocorrencia import Ocorrencia
from src.projeto import Projeto


class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.projetos = []

    def criar_funcionario(self, nome_funcionario):
        funcionario = Funcionario(nome_funcionario, len(self.funcionarios) + 1)
        self.funcionarios.append(funcionario)
        return funcionario

    def criar_projeto(self, nome_projeto):
        projeto = Projeto(nome_projeto, len(self.projetos) + 1)
        self.projetos.append(projeto)
        return projeto

    # def incluir_funcionario(self, funcionario):
    #     id_funcionario = len(self.funcionarios) + 1
    #     funcionario.id_funcionario = id_funcionario
    #     self.funcionarios.append(funcionario)
    #     return funcionario.id_funcionario
    #
    # def incluir_projeto(self, projeto):
    #     id_projeto = len(self.projetos) + 1
    #     projeto.id_projeto = id_projeto
    #     self.projetos.append(projeto)
    #     return projeto.id_projeto

    def obter_funcionario_por_id(self, id_funcionario):
        for funcionario in self.funcionarios:
            if funcionario.id_funcionario == id_funcionario:
                return funcionario

        return 'Funcionario inexistente'

    def obter_projeto_por_id(self, id_projeto):
        for projeto in self.projetos:
            if projeto.id_projeto == id_projeto:
                return projeto

        return 'Projeto inexistente'

    def incluir_funcionario_em_projeto(self, id_funcionario, id_projeto):

        # Checa se funcionario esta na empresa
        # se estiver, o retorna
        funcionario = self.obter_funcionario_por_id(id_funcionario)
        if funcionario == 'Funcionario inexistente':
            return funcionario

        # Checa se o projeto pertence a empresa
        # se pertencer, o retorna
        projeto = self.obter_projeto_por_id(id_projeto)
        if projeto == 'Projeto inexistente':
            return projeto

        # Checar se funcionario ja estã no projeto
        if id_funcionario in projeto.funcionarios:
            return 'Funcionario ja esta no projeto'

        projeto.funcionarios.append(id_funcionario)

        return 'Funcionario foi adicionado com sucesso'

    def obter_funcionarios_do_projeto(self, projeto_id):
        projeto = self.obter_projeto_por_id(projeto_id)
        if projeto == 'Projeto inexistente':
            return projeto

        funcionarios = []
        for id_funcionario in projeto.funcionarios:
            funcionario = self.obter_funcionario_por_id(id_funcionario)
            funcionarios.append(funcionario)

        return funcionarios

    def criar_ocorrencia_projeto(self, descricao, id_funcionario, id_projeto, tipo, prioridade):
        projeto = self.obter_projeto_por_id(id_projeto)
        if projeto == 'Projeto inexistente':
            return projeto

        funcionario = self.obter_funcionario_por_id(id_funcionario)
        if funcionario == 'Funcionario inexistente':
            return funcionario
        if self.check_atribuir_ocorrencia_funcionario(funcionario, projeto):
            ocorrencia = Ocorrencia(len(projeto.ocorrencias) + 1, descricao, id_funcionario, id_projeto, tipo, prioridade)
            projeto.ocorrencias.append(ocorrencia)
            funcionario.ocorrencias_atribuidas.append(ocorrencia.id_ocorrencia)
            return ocorrencia
        else:
            return 'Não é possível criar ocorrencia'

    def check_atribuir_ocorrencia_funcionario(self, funcionario, projeto):
        if funcionario.id_funcionario not in projeto.funcionarios:
            return False
        if len(funcionario.ocorrencias_atribuidas) >= 10:
            return False
        return True

    def obter_projeto_por_ocorrencia(self, ocorrencia):
        for projeto in self.projetos:
            if ocorrencia in projeto.ocorrencias:
                return projeto
        return 'Projeto inexistente'

    def reatribuir_ocorrencia(self, ocorrencia, id_funcionario):
        projeto = self.obter_projeto_por_ocorrencia(ocorrencia)
        funcionario = self.obter_funcionario_por_id(id_funcionario)
        if funcionario == 'Funcionario inexistente':
            return funcionario

        if projeto != 'Projeto inexistente' and self.check_atribuir_ocorrencia_funcionario(funcionario, projeto):
            ocorrencia.id_funcionario_responsavel = id_funcionario
            return ocorrencia
        else:
            return 'Erro ao reatribuir ocorrencia'