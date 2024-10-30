class Ocorrencia:
    def __init__(self, id_ocorrencia, descricao, id_funcionario_responsavel, id_projeto, tipo, prioridade):
        self.id_ocorrencia = id_ocorrencia
        self.descricao = descricao
        self.id_funcionario_responsavel = id_funcionario_responsavel
        self.id_projeto = id_projeto
        self.tipo = tipo
        self.prioridade = prioridade
        self.estado = 'Aberta'