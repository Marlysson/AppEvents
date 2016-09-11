# -*- coding: utf-8 -*-


#Bibliotecas padrão
import unittest
import sys,os

# Adicionando pasta externa para capturar os modelos externos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

from services.duracao import Duracao
from services.horario import Horario

from abstracoes.exceptions import DuracaoDeTempoInvalida

class TestaDuracao(unittest.TestCase):

	def test_deve_retornar_duracao_de_atividade_corretamente(self):

		inicio = Horario("10/10/2016 15:00")

		duracao = Duracao(inicio,durando="40 minutos")

		duracao = (duracao.final.com_horas - duracao.inicio.com_horas).seconds / 60

		self.assertEqual(duracao,40)

	def test_deve_gerar_excecao_ao_associar_duracao_invalida(self):

		inicio = Horario("12/12/2016 20:00")

		with self.assertRaises(DuracaoDeTempoInvalida):
			duracao = Duracao(inicio,durando="0 segundo")


if __name__ == "__main__":
	unittest.main(verbosity=2)