# -*- coding: utf-8 -*-

import unittest
import sys,os

pasta_projeto = os.path.abspath("../")
sys.path.append(pasta_projeto)

from modelo.atividade import Atividade
from enums.tipo_status import Status
from enums.tipo_atividade import TipoAtividade
from modelo.evento import Evento

class TestEvento(unittest.TestCase):
	
	def setUp(self):

		from datetime import datetime,date

		self.evento = Evento("Semana de informática","asdasdasd",date.today())

		self.palestra = Atividade(TipoAtividade.PALESTRA,"Semana de informática",datetime.now())
		self.tutorial = Atividade(TipoAtividade.TUTORIAL,"Semana de informática",datetime.now())
		self.mini_curso = Atividade(TipoAtividade.MINI_CURSO,"Semana de informática",datetime.now())

	def test_evento_criado_com_status_aberto(self):
		self.assertEqual("Aberto",str(self.evento.status))

	def test_evento_criado_alterado_seu_status(self):
		self.evento.status = Status.EM_ANDAMENTO

		self.assertEqual(str(self.evento.status),"Em Andamento")

	def test_evento_recem_criado_deve_ter_zero_atividades(self):
		self.assertEqual(0,len(self.evento.atividades))

	def test_evento_com_atividades_adicionadas(self):
		self.evento.add_atividade(self.palestra)
		self.evento.add_atividade(self.tutorial)
		self.evento.add_atividade(self.mini_curso)

		self.assertEqual(3,len(self.evento.atividades))

	@unittest.skip("Não implementado")
	def test_nao_deve_aceitar_eventos_data_passada(self):
		pass

	@unittest.skip("Não implementado")
	def test_deve_settar_automaticamente_em_inscricao_este_evento(self):
		pass

	@unittest.skip("Não implementado")
	def test_deve_aceitar_eventos_com_data_hoje_ou_futura(self):
		pass

	@unittest.skip("Não implementado")
	def test_deve_criar_evento_com_nome_e_descricao_nao_publicado(self):
		pass


if __name__ == "__main__":
	unittest.main(verbosity=2)
