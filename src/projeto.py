class Projeto:
    def __init__(self, nome, id_projeto=None):
        self.nome = nome
        self.id_projeto = id_projeto
        self.funcionarios = []


    # def obter_funcionario(self, id):
    #     for funcionario in self.funcionarios:
    #         if funcionario.id_funcionario == id:
    #             return funcionario
