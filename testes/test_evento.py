# -*- coding: utf-8 -*-

import unittest
import sys,os
from datetime import datetime, timedelta

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

#Modelos
from modelo.atividades import AtividadeSimples
from modelo.evento import Evento

#Enums
from enums.status_evento import StatusEvento
from enums.tipo_atividade import TipoAtividade

#Excecoes
from abstracoes.exceptions import EventoDataInvalida
from abstracoes.exceptions import AtividadeJaExisteNoEvento

#Services
from services.horario import Horario
from services.duracao import Duracao

from abstracoes.observers_concretos import Logger

class TestEvento(unittest.TestCase):
		
	def setUp(self):
		
		logger = Logger('../novas_atividades.txt')

		self.hoje = Horario()

		data_inicio = self.hoje.mais("10 dias")

		duracao = Duracao(data_inicio,durando="3 dias")

		self.evento = Evento("Semana de informática","asdasdasd",duracao)

		self.evento.registrar(logger)
		
		self.palestra = AtividadeSimples(TipoAtividade.PALESTRA,"Acessibilidade Web",self.hoje,0.0)
		self.tutorial = AtividadeSimples(TipoAtividade.TUTORIAL,"Javascript funcional",self.hoje,15.00)
		self.mini_curso = AtividadeSimples(TipoAtividade.MINI_CURSO,"Javascript - Best Pratices",self.hoje,30.00)
	
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

		for atividade in [self.palestra,self.tutorial,self.mini_curso]:
			self.evento.adicionar_atividade(atividade)

		self.assertEqual(3,len(self.evento.atividades))
	
	def test_nao_deve_aceitar_eventos_data_passada(self):
		
		data_inicio = Horario("1/1/2015 12:00")

		duracao = Duracao(data_inicio,durando="3 dias")

		with self.assertRaises(EventoDataInvalida):
			evento_erro = Evento("Python Day","Evento de Python",duracao)
	
	def test_deve_aceitar_eventos_com_data_hoje_ou_futura(self):

		duracao1 = Duracao(self.hoje,durando="2 dias")
		
		inicio2 = self.hoje.mais("10 dias")
		duracao2 = Duracao(inicio2,durando="10 dias")

		evento1 = Evento("Python Beach","Python na praia",duracao1)

		evento2 = Evento("Java Day","Java na Prática",duracao2)
	
	def test_deve_gerar_excecao_quando_adicionar_atividades_repetidas_no_evento(self):
		
		inicio = self.hoje.mais("2 dias")

		duracao = Duracao(inicio,durando="2 dias")

		evento = Evento("Python Beach","Python na praia",duracao)

		with self.assertRaises(AtividadeJaExisteNoEvento):
			
			for atividade in [self.tutorial,self.mini_curso,self.tutorial]:
				evento.adicionar_atividade(atividade)
			

if __name__ == "__main__":
	unittest.main(verbosity=2)