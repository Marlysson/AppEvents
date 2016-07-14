# -*- coding: utf-8 -*-
import sys,os

# Adicionando pasta externa para capturar os modelos
pasta_projeto = os.path.abspath("../")
sys.path.append(pasta_projeto)

from enums.tipo_status import Status
from datetime import datetime

class Evento(object):
	def __init__(self,nome,descricao,data_ocorrencia):
		self.nome = nome
		self.descricao = descricao
		self.data_inicio = data_ocorrencia
		self.data_final  = None
		self.status = Status.ABERTO
		self.status_inscricoes = Status.ABERTO
		self.atividades = list()
		self.inscricoes = list()
		self.local = None

	def add_atividade(self,atividade):
		self.atividades.append(atividade)

	def add_inscricaoelf,inscricao):
		self.inscricoes.append(inscricao)
		