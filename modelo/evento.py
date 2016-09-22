# -*- coding: utf-8 -*-

import sys,os
from datetime import datetime , date , timedelta

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

from modelo.cupom import Cupom

from enums.status_evento import StatusEvento

#Abstracoes
from abstracoes.exceptions import EventoDataInvalida
from abstracoes.exceptions import AtividadeJaExisteNoEvento
from abstracoes.exceptions import InscricaoJaExisteNoEvento
from abstracoes.exceptions import PeriodoInvalidoParaInscricoes
from abstracoes.descontos import DescontoNulo

#Services
from services.horario import Horario
from services.duracao import Duracao

from abstracoes.observer import Subject

class Evento(Subject):

	def __init__(self,nome,descricao,duracao):

		self.nome          = nome
		self.descricao     = descricao
		
		self.duracao       = duracao

		self.visibilidade  = StatusEvento.NAO_PUBLICADO
		self.ocorrencia    = StatusEvento.NAO_INICIADO
		
		self.prazo_inscricoes = None
		
		self.atividades    = list()
		self.inscricoes    = list()
		self.inscricoes_confirmadas = list()
		
		validade = Horario().mais("1 dia")
		cupom_nulo = Cupom("CupomNulo",0.0,validade,DescontoNulo)
		
		self.cupons        = [ cupom_nulo ]

		self.local         = None

		self.eventos_satelites = list()
		self.evento_pai = None

		self.inscricao_unica = False
		
		self.espacos_fisicos = list()

		self.observadores = list()

	def __eq__(self,evento):

		if self.__dict__ == evento.__dict__:
			return True
		return False
	
	@property
	def horario_inicio(self):
		return self.duracao.inicio

	@property
	def horario_final(self):
		return self.duracao.final

	@property
	def duracao(self):
		return self._duracao

	@duracao.setter
	def duracao(self,duracao):
		
		hoje = Horario()

		if duracao.horario_inicio.com_horas < hoje.com_horas:
			raise EventoDataInvalida("Data de Início Inválida")
	
		self._duracao = duracao		
			
	@property
	def ocorrencia(self):
		return self._ocorrencia

	@ocorrencia.setter
	def ocorrencia(self,status):
		self._ocorrencia = status

	def adicionar_atividade(self,atividade):


		if atividade in self.atividades:
			raise AtividadeJaExisteNoEvento("Atividade Já Existe")
		else:
			self.atividades.append(atividade)

		self.notificar("Atividade adicionada : {}".format(atividade.descricao))

	def mudar_visibilidade(self,visibilidade):

		possiveis_visibilidade = [StatusEvento.PUBLICADO,StatusEvento.NAO_PUBLICADO]

		if not visibilidade in possiveis_visibilidade:
			raise ValueError("Visibilidade Inválida")

		self.visibilidade = visibilidade

	def apto_a_inscricoes(self):

		hoje = Horario()

		if self.prazo_inscricoes.data >= hoje.data:
			return True
		else:
			return False		

	def adicionar_inscricao(self,inscricao):

		if not self.apto_a_inscricoes():
			raise PeriodoInvalidoParaInscricoes("Prazo encerrado de inscrições")

		if inscricao in self.inscricoes:
			raise InscricaoJaExisteNoEvento("Inscrição já existe no evento")
		
		self.inscricoes.append(inscricao)
	
	def adicionar_cupom(self,cupom):
		self.cupons.append(cupom)

	def adicionar_espaco(self,espaco):
		self.espacos_fisicos.append(espaco)

	def evento_relacionado(self,evento):

		if (evento in self.eventos_satelites):
			raise ValueError("Evento satélite já cadastrado")

		self.eventos_satelites.add(evento)
		evento.evento_pai = self

	def gerar_agenda(self):

		lista_atividades = []

		if len(self.eventos_satelites) == 0:
			for espaco in self.espacos_fisicos:
				atividades = espaco.gerar_agenda()
				lista_atividades.append(atividades)
		else:

			for evento in self.eventos_satelites:
				for atividade in self.evento.atividades:
					atividades = evento.gerar_agenda()
					lista_atividades.append(atividades)

		return list(self.organizar_lista(lista_atividades))

	def organizar_lista(self,lista):

		for atividade in lista:
			if isinstance(atividade,list):
				for atividades in self.organizar_lista(atividade):
					yield atividades
			else:
				yield atividade

	def registrar(self,observer):
		self.observadores.append(observer)

	def remover(self,observer):
		self.observadores.remove(observers)

	def notificar(self,mensagem):
		for observador in self.observadores:
			observador.update(mensagem)

	def __repr__(self):
		return "{}".format(self.__dict__)