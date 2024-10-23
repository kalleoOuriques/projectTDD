import unittest

from statsmodels.tools.testing import assert_equal

from src.empresa import Empresa


class TestEmpresa(unittest.TestCase):
    def test_criar_empresa(self):
        nome = "Bradesco"
        empresa = Empresa(nome)
        assert_equal(empresa.nome, nome)
