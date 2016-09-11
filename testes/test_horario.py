# -*- coding: utf-8 -*-

import unittest
import sys,os

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

from abstracoes.horario import Horario
from datetime import datetime , date , timedelta

class TestHorario(unittest.TestCase):

	def setUp(self):
		self.horario = Horario("2/1/2015 16:00")
		self.horario_padrao = Horario()

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

		self.assertEqual(data_nativa,self.horario.data)

	def test_deve_retornar_formato_nativo_da_parte_completa_do_horario(self):

		datetime_nativo = datetime(2015,1,2,16,0,0)

		self.assertEqual(datetime_nativo,self.horario.com_horas)

	def test_nao_deve_gerar_excecao_com_horario_faltando_segundos(self):

		horario = Horario("07/09/2016 15:00")

	def test_deve_somar_corretamente_dias_ao_horario_dado(self):

		dois_dias = datetime.now().date() + timedelta(days=2)

		horario = Horario().mais("2 dias").data

		self.assertEqual(dois_dias,horario)

	def test_deve_retornar_horario_correto_quando_somar_meses(self):

		horario = Horario("01/11/2016 16:00").mais("2 meses").com_horas

		data_posterior = datetime(2016,12,31,16,0,0)

		self.assertEqual(horario,data_posterior)

	def test_deve_retornar_horario_correto_quando_adicionar_minutos(self):

		horario = Horario("31/12/2016 23:59").mais("2 minutos").com_horas

		janeiro = datetime(2017,1,1,0,1)

		self.assertEqual(horario,janeiro)

	def test_representacao_do_horario_corretamente(self):

		horario = str(Horario("10/11/2013 16:22"))

		self.assertEqual(horario,"10/11/2013 16:22")

if __name__ == "__main__":
	unittest.main(verbosity=2)