# -*- coding: utf-8 -*-

import unittest
import sys,os

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

from abstracoes.horario import Horario
from datetime import datetime,date

class TestHorario(unittest.TestCase):

	def setUp(self):
		self.horario = Horario("2/1/2015 16:00")

	def test_horario_deve_gerar_excecao_com_valores_invalidos(self):

		with self.assertRaises(ValueError):
			horario = Horario("01/25/2015 15:00")

	def test_deve_retornar_dia_correto_do_horario_definido(self):
		self.assertEqual(2,self.horario.dia)

	def test_deve_retornar_ano_correto_do_horario_definido(self):
		self.assertEqual(2015,self.horario.ano)

	def test_deve_retornar_hora_correta_do_horario_definido(self):
		self.assertEqual(16,self.horario.hora)

	def test_deve_retornar_formato_nativo_da_parte_de_data_do_horario(self):

		data_nativa = date(2015,1,2)

		self.assertEqual(data_nativa,self.horario.date)

	def test_deve_retornar_formato_nativo_da_parte_completa_do_horario(self):

		datetime_nativo = datetime(2015,1,2,16,0,0)

		self.assertEqual(datetime_nativo,self.horario.datetime)

	def test_nao_deve_gerar_excecao_com_horario_faltando_segundos(self):

		horario = Horario("07/09/2016 15:00")
			
if __name__ == "__main__":
	unittest.main(verbosity=2)