import unittest

from statsmodels.tools.testing import assert_equal

from src.empresa import Empresa


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

    def test_inclusao_multiplos_projetos(self):
        assistente_ia = self.empresa.criar_projeto('Assistente IA')
        loading_page = self.empresa.criar_projeto('Loading Page')
        mensageria = self.empresa.criar_projeto('Mensageria')

        assert_equal(self.empresa.projetos, [assistente_ia, loading_page, mensageria])

    def test_obter_funcionario_em_empresa(self):
        joao = self.empresa.criar_funcionario("João")
        jose = self.empresa.criar_funcionario("José")
        assert_equal(jose, self.empresa.obter_funcionario_por_id(jose.id_funcionario))

    def test_obter_projeto_em_empresa(self):
        app_banco_online = self.empresa.criar_projeto("App Banco Online")
        assert_equal(app_banco_online, self.empresa.obter_projeto_por_id(app_banco_online.id_projeto))

    def test_incluir_funcionario_em_projeto(self):
        joao = self.empresa.criar_funcionario("João")
        app_banco_online = self.empresa.criar_projeto("App Banco Online")

        self.empresa.incluir_funcionario_em_projeto(joao.id_funcionario, app_banco_online.id_projeto)

        assert_equal([joao], self.empresa.obter_funcionarios_do_projeto(app_banco_online.id_projeto))

    def test_obter_funcionarios_do_projeto(self):
        joao = self.empresa.criar_funcionario("João")
        jose = self.empresa.criar_funcionario("José")
        app_banco_online = self.empresa.criar_projeto("App Banco Online")
        self.empresa.incluir_funcionario_em_projeto(joao.id_funcionario, app_banco_online.id_projeto)
        self.empresa.incluir_funcionario_em_projeto(jose.id_funcionario, app_banco_online.id_projeto)

        funcionarios = self.empresa.obter_funcionarios_do_projeto(app_banco_online.id_projeto)

        assert_equal(funcionarios, [joao, jose])

    def test_incluir_duas_vezes_o_mesmo_funcionario(self):
        joao = self.empresa.criar_funcionario("João")
        app_banco_online = self.empresa.criar_projeto("App Banco Online")
        self.empresa.incluir_funcionario_em_projeto(joao.id_funcionario, app_banco_online.id_projeto)

        resultado_inclusao = self.empresa.incluir_funcionario_em_projeto(joao.id_funcionario, app_banco_online.id_projeto)

        assert_equal(resultado_inclusao,'Funcionario ja esta no projeto')

    # EX. 9

    def test_criar_ocorrencia(self):
        app_banco_online = self.empresa.criar_projeto("App Banco Online")
        descricao = 'Saque em conta com saldo insuficiente'
        joao = self.empresa.criar_funcionario("João")
        saque_saldo_insuficiente = self.empresa.criar_ocorrencia_projeto(descricao, joao, app_banco_online.id_projeto)
        assert_equal(saque_saldo_insuficiente.descricao, descricao)