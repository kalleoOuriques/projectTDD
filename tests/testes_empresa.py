import unittest

from statsmodels.tools.testing import assert_equal

from src.empresa import Empresa
from src.funcionario import Funcionario
from src.projeto import Projeto


class TestEmpresa(unittest.TestCase):
    def setUp(self):
        self.empresa = Empresa("Banco do Brasil")

    def test_criar_empresa(self):
        nome = "Bradesco"
        empresa = Empresa(nome)
        assert_equal(empresa.nome, nome)

    def test_criar_funcionario(self):
        nome = "João"
        funcionario = self.empresa.criar_funcionario(nome)
        assert_equal(funcionario.nome, nome)

    def test_criar_projeto(self):
        nome = "App Banco Online"
        projeto = self.empresa.criar_projeto(nome)
        assert_equal(projeto.nome, nome)

    def test_incluir_funcionario_em_empresa(self):
        joao = Funcionario("João")
        id_funcionario = self.empresa.incluir_funcionario(joao)
        assert_equal(joao.id_funcionario, id_funcionario)

    def test_incluir_projeto_em_empresa(self):
        app_banco_online = Projeto("App Banco Online")
        id_projeto = self.empresa.incluir_projeto(app_banco_online)
        assert_equal(app_banco_online.id_projeto, id_projeto)

    def test_obter_funcionario_em_empresa(self):
        joao = self.empresa.criar_funcionario("João")
        jose = self.empresa.criar_funcionario("José")
        self.empresa.incluir_funcionario(joao)
        self.empresa.incluir_funcionario(jose)
        # assert_equal(joao, self.empresa.obter_funcionario_por_id(joao.id_funcionario))
        assert_equal(jose, self.empresa.obter_funcionario_por_id(jose.id_funcionario))

    def test_obter_projeto_em_empresa(self):
        app_banco_online = Projeto("App Banco Online")
        self.empresa.incluir_projeto(app_banco_online)
        assert_equal(app_banco_online, self.empresa.obter_projeto_por_id(app_banco_online.id_projeto))

    def test_incluir_funcionario_em_projeto(self):
        joao = self.empresa.criar_funcionario("João")
        id_joao = self.empresa.incluir_funcionario(joao)
        app_banco_online = Projeto("App Banco Online")
        id_app_banco_online = self.empresa.incluir_projeto(app_banco_online)

        self.empresa.incluir_funcionario_em_projeto(joao, app_banco_online)

        assert_equal(joao, app_banco_online.obter_funcionario(id_joao))

    def test_obter_funcionario_em_projeto(self):
        joao = self.empresa.criar_funcionario("João")
        id_joao = self.empresa.incluir_funcionario(joao)
        app_banco_online = Projeto("App Banco Online")
        self.empresa.incluir_funcionario_em_projeto(joao, app_banco_online)

        funcionario_obtido = app_banco_online.obter_funcionario(id_joao)

        assert_equal(joao, funcionario_obtido)

    def test_incluir_duas_vezes_o_mesmo_funcionario(self):
        joao = self.empresa.criar_funcionario("João")
        id_joao = self.empresa.incluir_funcionario(joao)
        app_banco_online = Projeto("App Banco Online")
        id_app_banco_online = self.empresa.incluir_projeto(app_banco_online)
        self.empresa.incluir_funcionario_em_projeto(joao, app_banco_online)

        resultado_inclusao = self.empresa.incluir_funcionario_em_projeto(joao, app_banco_online)

        assert_equal(resultado_inclusao,'Funcionario ja esta no projeto')

