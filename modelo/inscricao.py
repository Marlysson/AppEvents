#-*- coding: utf-8 -*-


import sys,os
from datetime import datetime , date , timedelta

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

from abstracoes.exceptions import AtividadeNaoEncontradaNoEvento
from abstracoes.exceptions import AtividadeJaExisteNaInscricao
from abstracoes.exceptions import InscricaoJaPagaNaoAceitaItens

class Inscricao(object):

	def __init__(self,participante,evento):
		
		self.participante   = participante
		self.evento         = evento
		self.atividades     = []
		
		self.data_pagamento = None
		self.paga 			= False

		self.data_checkin = None

	def __eq__(self,inscricao):
		
		if self.__dict__ == inscricao.__dict__:
			return True
		return False

	@property
	def preco_total(self):
	    preco_total = 0.0

	    for atividade in self.atividades:
	    	preco_total += atividade.preco

	    return preco_total
	
	@property
	def cupons_evento(self):
		return self.evento.cupons

	def adicionar_atividade(self,atividade):

		if self.paga:
			raise InscricaoJaPagaNaoAceitaItens("Não é permitido mais inscrições")

		if not self.atividade_valida(atividade):
			raise AtividadeNaoEncontradaNoEvento("Atividade Não Encontrada")

		if atividade in self.atividades:
			raise AtividadeJaExisteNaInscricao("Atividade Já Existe")

		self.atividades.append(atividade)


	def atividade_valida(self,atividade):
		if atividade in self.evento.atividades:
			return True
		return False

	def realizar_checkin(self):
		from datetime import date
		hoje = date.today()

		self.evento.inscricoes_confirmadas.append(self)

		self.data_checkin = hoje