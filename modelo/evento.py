# -*- coding: utf-8 -*-
import sys,os

# Adicionando pasta externa para capturar os modelos
pasta_projeto = os.path.abspath("../")
sys.path.append(pasta_projeto)

from enums import Status

class Evento(object):
	def __init__(self,nome,descricao,data_ocorrencia):
		self.nome = nome
		self.descricao = desccricao
		self.data_inicio = data_ocorrencia
		self.status = Status.ABERTO
		self.status_inscricoes = Status.ABERTO
		self.inscricoes = list()
		self.atividades = list()
		self.local = None

	def add_atividades(self,atividade):
		self.atividades.append(atividade)

	def add_inscricoes(self,inscricao):
		self.inscricoes.append(inscricao)

		
