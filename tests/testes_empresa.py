import unittest

from statsmodels.tools.testing import assert_equal

from src.empresa import Empresa
from src.funcionario import Funcionario


class TestEmpresa(unittest.TestCase):
    def test_criar_empresa(self):
        nome = "Bradesco"
        empresa = Empresa(nome)
        assert_equal(empresa.nome, nome)

    def test_criar_funcionario(self):
        nome = "João"
        funcionario = Funcionario(nome)
        assert_equal(funcionario.nome, nome)