# -*- coding: utf-8 -*-

import sys,os
from datetime import datetime

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

from enums.status_evento import StatusEvento

from abstracoes.exceptions import EventoDataInvalida
from abstracoes.exceptions import AtividadeJaExisteNoEvento
from abstracoes.exceptions import InscricaoJaExisteNoEvento

class Evento(object):
	def __init__(self,nome,descricao,data_inicio,data_final):
		self.nome          = nome
		self.descricao     = descricao
		self.data_inicio   = data_inicio
		self.data_final    = data_final
		self.visibilidade  = StatusEvento.NAO_PUBLICADO
		self.ocorrencia    = StatusEvento.NAO_INICIADO
		self.prazo_inscricoes = None
		
		self.atividades    = list()
		self.inscricoes    = list()
		
		self.local         = None

	def __eq__(self,evento):

		if self.__dict__ == evento.__dict__:
			return True
		return False

	@property
	def data_inicio(self):
		return self._data_inicio

	@data_inicio.setter
	def data_inicio(self,data):

		hoje = datetime.now()

		if data < hoje:
			raise EventoDataInvalida("Data de Início Inválida")
		else:
			self._data_inicio = data
			
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


	def mudar_visibilidade(self,visibilidade):

		possiveis_visibilidade = [StatusEvento.PUBLICADO,StatusEvento.NAO_PUBLICADO]

		if not visibilidade in possiveis_visibilidade:
			raise ValueError("Visibilidade Inválida")

		self.visibilidade = visibilidade

	def inscricoes_disponiveis(self):

		hoje = datetime.now()

		if self.prazo_inscricoes <= hoje:
			return True
		else:
			return False		

	def adicionar_inscricao(self,inscricao):

		if inscricao in self.inscricoes:
			raise InscricaoJaExisteNoEvento("Inscrição já existe no evento")
		else:
			self.inscricoes.append(inscricao)
		
	def __repr__(self):
		return "{}".format(self.__dict__)