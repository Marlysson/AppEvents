
import unittest
import sys,os

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

from modelo.atividade import AtividadeSimples , KitAtividade
from enums.tipo_atividade import TipoAtividade
from services.horario import Horario

class TestComboAtividades(unittest.TestCase):

	def setUp(self):

		self.horario1 = Horario("10/11/2017 10:00")
		self.horario2 = self.horario1.mais("2 horas")
		self.horario3 = self.horario2.mais("50 minutos")

		self.tdd  = AtividadeSimples(TipoAtividade.TUTORIAL,"Introdução à TDD",self.horario1,15.00)
		self.hackathon = AtividadeSimples(TipoAtividade.HACKATHON,"Soluções Inteligentes",self.horario2,50.00)
		self.workshop  = AtividadeSimples(TipoAtividade.WORKSHOP,"Hackeando Dados Públicos",self.horario2,20.00)

		self.jsf = AtividadeSimples(TipoAtividade.TUTORIAL,"Java pra Web",self.horario1,10.00)
		self.primefaces = AtividadeSimples(TipoAtividade.PALESTRA,"Framework Web Java",self.horario2,20.00)
		self.junit = AtividadeSimples(TipoAtividade.WORKSHOP,"Testando aplicações Java",self.horario3,20.00)

	def test_deve_gerar_excecao_se_atividade_simples_adicionar_atividades(self):

		with self.assertRaises(TypeError):
			self.tdd.add(self.hackathon)


	def test_deve_retornar_preco_de_combo_com_logica_aplicada_aos_seus_precos(self):

		kit_java = KitAtividade("Kit Javeiro")

		for atividade in [self.jsf , self.primefaces , self.junit]:
			kit_java.add(atividade)

		preco_kit_java = kit_java.preco_total

		self.assertEqual(50.00,preco_kit_java)

	def test_misturando_atividades_simples_com_compostas_em_um_kit(self):

		kit_python = KitAtividade("Pythonista")
		kit_java   = KitAtividade("Javeiro")
		kit_geral  = KitAtividade("Melhores Práticas Dev")

		for atividade in [ self.tdd , self.workshop]:
			kit_python.add(atividade)

		for atividade in [self.junit , self.primefaces]:
			kit_java.add(atividade)

		for kit in [ kit_java , kit_python]:
			kit_geral.add(kit)
			
		kit_geral.add(self.jsf)

		self.assertEqual(85.00,kit_geral.preco_total)

if __name__ == "__main__":
	unittest.main(verbosity=2)