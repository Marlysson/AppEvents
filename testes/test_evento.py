# -*- coding: utf-8 -*-

import unittest
import sys,os
from datetime import datetime, timedelta

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

#Modelos
from modelo.atividade import Atividade
from modelo.evento import Evento

#Enums
from enums.status_evento import StatusEvento
from enums.tipo_atividade import TipoAtividade

#Excecoes
from abstracoes.exceptions import EventoDataInvalida

#Abstrações
from abstracoes.horario import Horario


class TestEvento(unittest.TestCase):
	
	def setUp(self):


		data_inicio = datetime.now() + timedelta(10)

		data_finalizacao = data_inicio + timedelta(days=3)

		self.evento = Evento("Semana de informática","asdasdasd",data_inicio,data_finalizacao)

		self.palestra = Atividade(TipoAtividade.PALESTRA,"Semana de informática",datetime.now(),0.0)
		self.tutorial = Atividade(TipoAtividade.TUTORIAL,"Semana de informática",datetime.now(),15.00)
		self.mini_curso = Atividade(TipoAtividade.MINI_CURSO,"Semana de informática",datetime.now(),30.00)

	def test_deve_criar_evento_com_nome_e_descricao_nao_publicado(self):
		self.assertEqual(StatusEvento.NAO_PUBLICADO,self.evento.visibilidade)

	def test_deve_alterar_visibilidade_valida_do_evento(self):

		self.evento.mudar_visibilidade(StatusEvento.PUBLICADO)

		self.assertEqual(StatusEvento.PUBLICADO,self.evento.visibilidade)

	def test_deve_retornar_exception_com_visibilidade_invalida(self):

		with self.assertRaises(ValueError):
			self.evento.mudar_visibilidade("Visibilidade Inválida")

	def test_deve_iniciar_evento_com_status_nao_iniciado(self):
		self.assertEqual(StatusEvento.NAO_INICIADO,self.evento.ocorrencia)

	def test_evento_recem_criado_deve_ter_zero_atividades(self):
		
		self.assertEqual(0,len(self.evento.atividades))

	def test_evento_com_atividades_adicionadas(self):

		self.evento.adicionar_atividade(self.palestra)
		self.evento.adicionar_atividade(self.tutorial)
		self.evento.adicionar_atividade(self.mini_curso)

		self.assertEqual(3,len(self.evento.atividades))

	def test_nao_deve_aceitar_eventos_data_passada(self):
		
		data_inicio = datetime(2015,1,1,12,0,0)

		data_final = data_inicio + timedelta(days=3)

		with self.assertRaises(EventoDataInvalida):
			evento_erro = Evento("Python Day","Evento de Python",data_inicio,data_final)

	def test_deve_aceitar_eventos_com_data_hoje_ou_futura(self):
		
		hoje = datetime.now()

		inicio1 = hoje + timedelta(days=1)
		final1 = inicio1 + timedelta(days=2)

		inicio2 = hoje + timedelta(days=10)
		final2 = inicio2 + timedelta(days=2)

		evento1 = Evento("Python Beach","Python na praia",inicio1,final1)

		evento2 = Evento("Java Day","Java na Prática",inicio2,final2)


	@unittest.skip("Não implementado")
	def test_deve_settar_automaticamente_em_inscricao_este_evento(self):
		pass

if __name__ == "__main__":
	unittest.main(verbosity=2)