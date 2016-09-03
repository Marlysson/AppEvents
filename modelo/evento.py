# -*- coding: utf-8 -*-
import sys,os

# Adicionando pasta externa para capturar os modelos
pasta_projeto = os.path.abspath("../")
sys.path.append(pasta_projeto)

from enums.tipo_status import Status
from datetime import datetime

class Evento(object):
	def __init__(self,nome,descricao,data_inicio):
		self.nome = nome
		self.descricao = descricao
		self.data_inicio = data_inicio
		self.data_final  = None
		self.status = Status.ABERTO
		self.prazo_inscricoes = None
		self.atividades = list()
		self.inscricoes = list()
		self.local = None

	def add_atividade(self,atividade):
		self.atividades.append(atividade)

	def add_inscricao(inscricao):
		self.inscricoes.append(inscricao)
		