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
        id_projeto = 1
        self.empresa.incluir_projeto(app_banco_online)
        assert_equal(id_projeto, len(self.empresa.projetos))