# -*- coding: utf-8 -*-

import unittest
import sys,os

# Adicionando pasta externa para capturar os modelos
pasta_projeto = os.path.abspath("../")
sys.path.append(pasta_projeto)

from modelo.evento import Evento
from modelo.atividades import *
from enums.tipo_status import Status

class TestEvento(unittest.TestCase):
	
	def setUp(self):

		from datetime import datetime

		self.evento = Evento("Semana de informática","asdasdasd",datetime.now())

		self.palestra = Palestra("Palestra 1")
		self.tutorial = Tutorial("Tutorial 1")
		self.mini_curso = Tutorial("Tutorial 1")

	def test_evento_criado_sem_atividades(self):
		self.assertEqual(0,len(self.evento.atividades))

	def test_evento_criado_com_status_aberto(self):
		self.assertEqual("Aberto",str(self.evento.status))

	def test_evento_criado_alterado_seu_status(self):
		self.evento.status = Status.EM_ANDAMENTO

		self.assertEqual(str(self.evento.status),"Em Andamento")

	def test_evento_criado_sem_inscricoes(self):
		self.assertEqual(0,len(self.evento.inscricoes))

	def test_evento_com_atividades_adicionadas(self):
		self.evento.add_atividade(self.palestra)
		self.evento.add_atividade(self.tutorial)
		self.evento.add_atividade(self.mini_curso)

		self.assertEqual(3,len(self.evento.atividades))

if __name__ == "__main__":
	unittest.main()
