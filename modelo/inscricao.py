#-*- coding: utf-8 -*-

from datetime import datetime

class Inscricao(object):

	def __init__(self,participante,evento):
		self.participante   = participante
		self.evento         = evento
		self.atividades     = []
		self.cupom          = None
		self.data_pagamento = None

		self.evento._inscricao(self)

	@property
	def paga(self):
		return ( self.data_pagamento - datetime.now() ).days < 0

	@property
	def preco_total(self):
		resultado = 0.0

		for atividade in atividades:
			resultado += atividade.preco

		return resultado

	def add_atividade(self,atividade):
		if atividade in self.evento.atividades:
			self.atividades.append(atividade)
		else:
			raise Exception("Atividade nao existente no evento.")

	def add_cupom(self,cupom):
		self.cupons.append(cupom)
