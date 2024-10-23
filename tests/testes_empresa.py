import unittest

from statsmodels.tools.testing import assert_equal

from src.empresa import Empresa
from src.funcionario import Funcionario


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

    def test_incluir_funcionario_em_empresa(self):
        joao = Funcionario("João")
        id = 1
        self.empresa.incluir_funcionario(joao)
        assert_equal(len(self.empresa.funcionarios), id)