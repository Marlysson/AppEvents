#-*- coding: utf-8 -*-

from datetime import datetime

class Inscricao(object):

	def __init__(self,participante,evento):
		self.participante   = participante
		self.evento         = evento
		self.atividades     = list()
		self.cupons         = list()
		self.data_pagamento = None

		@property
		def paga(self):
			return ( self.data_pagamento - datetime.now() ).days < 0

		@property
		def preco(self):
			resultado = 0.0

			for atividade in atividades:
				resultado += atividade.preco

			return resultado

		def pagar(self,valor):
			if valor <= self.preco:
				return False
			elif valor == self.preco:
				return True

		def add_atividade(self,atividade):
			if atividade in self.evento.atividades:
				self.atividades.append(atividade)
			else:
				#Subir exceção AtividadeNaoEncontrada
				

		def add_cupon(self,cupom):
			self.cupons.append(cupom)

'''
insc = Inscricao(participante,evento)
insc.add_atividade(tutorial)
insc.add_atividade(minicurso)
insc.data_pagamento(datetime.now())
'''