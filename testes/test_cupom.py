# -*- coding : utf8 -*- 

import unittest

import sys,os

# Adicionando pasta externa para capturar os modelos
pasta_projeto = os.path.abspath("../")
sys.path.append(pasta_projeto)

from modelo.cupom import Cupom

class TestCupom(unittest.TestCase):

	def test_deve_ser_ativo_se_estar_no_periodo_da_validade(self):
		from datetime import date

		cupom = Cupom("PALESTRA_50",0.5,date(2016,07,23))

		validade = cupom.valido()

		self.assertTrue(validade)

	def test_nao_deve_ser_ativo_se_estiver_fora_da_validade(self):
		from datetime import date

		cupom = Cupom("PALESTRA_50",0.5,date(2016,07,25))

		validade = cupom.valido()

		self.assertFalse(validade)

if __name__ == "__main__":
	unittest.main()
