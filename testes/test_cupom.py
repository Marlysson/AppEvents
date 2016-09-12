# -*- coding : utf8 -*- 

import os , sys
import unittest
from datetime import date , timedelta

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

from services.horario import Horario
from modelo.cupom import Cupom
from abstracoes.descontos import DescontoNulo

class TestCupom(unittest.TestCase):

	def test_deve_ser_ativo_se_estar_no_periodo_da_validade(self):
		
		validade_futura = Horario().mais("7 dias")
		cupom = Cupom("ANDROID_10",0.1,validade_futura)

		validade = cupom.valido

		self.assertTrue(validade)

	def test_nao_deve_ser_ativo_se_estiver_fora_da_validade(self):

		validade = Horario("11/11/2011 10:00")

		cupom = Cupom("BAIXA_TUDO_10",0.1,validade)

		validade = cupom.valido

		self.assertFalse(validade)

	def test_deve_validar_um_cupom_nulo(self):

		validade = Horario().mais("7 dias")

		cupom_nulo = Cupom("CupomNulo",0.0,validade,DescontoNulo)
		
		self.assertTrue(cupom_nulo.valido)


if __name__ == "__main__":
	unittest.main(verbosity=2)
