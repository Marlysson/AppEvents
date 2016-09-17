# -*- coding : utf-8 -*-
import sys,os

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

from abstracoes.espaco_fisico import EspacoFisico
from modelo.localizacao import Local

class EspacoSimples(EspacoFisico):
	
	'''
		:descricao   str
		:capacidade  int
		:local       Local
		:atividade   ItemEvento
	'''

	def __init__(self,descricao,capacidade,local):
		self.descricao  = descricao
		self.capacidade = capacidade
		self.local 		= local

		self.atividade  = None

	@property
	def inscritos(self):
		return self.atividade.inscritos

	def gerar_agenda(self):
		return self.atividade

class EspacoComposto(EspacoFisico):
	
	'''
		:descricao  str
		:local 		Local
		:espacos    list<EspacoFisico>
	'''

	def __init__(self,descricao,local):
		self.descricao = descricao
		self.local 	   = local
		self.espacos   = list()

	@property
	def capacidade(self):
		capacidade = 0

		for espaco in self.espacos:
			capacidade += espaco.capacidade

		return capacidade

	@property
	def inscritos(self):
		pessoas = []

		for espaco in self.espacos:
			pessoas.append(espaco.inscritos)

		return pessoas

	def gerar_agenda(self):
		atividades = []

		for atividade in self.espacos:
			atividades = atividade.gerar_agenda()

			atividades.append(atividades)

		return atividades

	def add(self,espaco):
		self.espacos.append(espaco)

	def remover(self,espaco):
		self.espacos.remove(espaco)