# -*- coding : utf8 -*- 

import unittest
from datetime import datetime , timedelta
import os , sys

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

from modelo.cupom import Cupom
from enums.tipo_atividade import TipoAtividade

class TestCupom(unittest.TestCase):

	def test_deve_ser_ativo_se_estar_no_periodo_da_validade(self):
		from datetime import date , timedelta

		validade_futura = date.today() + timedelta(days=7)

		cupom = Cupom("PROGRAMACAO_ANDROID_10",0.1,validade_futura)

		validade = cupom.validar()

		self.assertTrue(validade)

	def test_nao_deve_ser_ativo_se_estiver_fora_da_validade(self):
		from datetime import date , timedelta

		hoje = date.today()
		dia_anterior = hoje - timedelta(days=1)

		cupom = Cupom("MINI_CURSOS_10",0.1,dia_anterior)

		validade = cupom.validar()

		self.assertFalse(validade)

	def test_deve_retornar_cupons_iguais_criados(self):

		hoje = datetime.now()
		
		validade = hoje + timedelta(1)

		cupom1 = Cupom("SETEMBRO_10",0.1,validade)
		cupom2 = Cupom("SETEMBRO_10",0.1,validade)

		self.assertEqual(cupom1,cupom2)

	def test_deve_retornar_cupons_diferentes(self):

		hoje = datetime.now()
		
		validade = hoje + timedelta(1)		

		cupom1 = Cupom("PALESTRAS_50",0.5,validade)
		cupom2 = Cupom("PALESTRAS_50",0.1,validade)

		self.assertNotEqual(cupom1,cupom2)		
		
if __name__ == "__main__":
	unittest.main()
