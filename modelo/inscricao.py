#-*- coding: utf-8 -*-


import sys,os
from datetime import datetime

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

from abstracoes.exceptions import AtividadeNaoEncontradaNoEvento
from abstracoes.exceptions import AtividadeJaExisteNaInscricao

class Inscricao(object):

	def __init__(self,participante,evento):
		self.participante   = participante
		self.evento         = evento
		self.atividades     = []
		self.cupom          = None
		self.data_pagamento = None

		self.evento.adicionar_inscricao(self)

	def __eq__(self,inscricao):
		
		if self.__dict__ == inscricao.__dict__:
			return True
		return False

	def adicionar_atividade(self,atividade):

		if atividade in self.evento.atividades:
			
			if atividade in self.atividades:
				raise AtividadeJaExisteNaInscricao("Atividade Já Existe")
			else:
				self.atividades.append(atividade)

		else:
			raise AtividadeNaoEncontradaNoEvento("Atividade Não Encontrada")

	def adicionar_cupom(self,cupom):
		self.cupom = cupom
