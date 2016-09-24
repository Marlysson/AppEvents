# -*- coding : utf8 -*- 

import os , sys
import unittest
from datetime import date , timedelta

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
sys.path.append(diretorio_atual)

from services.horario import Horario
from fabricas.cupom_factory import CupomFactory

class TestCupom(unittest.TestCase):

	def test_deve_ser_ativo_se_estar_no_periodo_da_validade(self):
		
		validade_futura = Horario().mais("7 dias")

		cupom = CupomFactory.obter("ANDROID_10",0.1,validade_futura)

		self.assertTrue(cupom.valido)

	def test_nao_deve_ser_ativo_se_estiver_fora_da_validade(self):

		validade = Horario("11/11/2011 10:00")

		cupom = CupomFactory.obter("BAIXA_TUDO_10",0.1,validade,"tutorial")

		self.assertFalse(cupom.valido)

	def test_deve_validar_um_cupom_nulo(self):

		validade = Horario().mais("7 dias")

		cupom_padrao = CupomFactory.obter("Padrão",0,validade)

		self.assertTrue(cupom_padrao.valido)


if __name__ == "__main__":
	unittest.main(verbosity=2)
