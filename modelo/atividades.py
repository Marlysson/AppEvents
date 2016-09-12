# -*- coding : utf-8 -*-

import sys,os

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

from abstracoes.item_evento import ItemEvento

class AtividadeSimples(ItemEvento):
	def __init__(self,tipo,descricao,duracao,preco=0.0):
		self.tipo = tipo
		self.descricao = descricao
		self.duracao = duracao
		self.preco = float(preco)


	@property
	def horario_inicio(self):
		return self.duracao.inicio

	@property
	def horario_final(self):
		return self.duracao.final

	@property
	def preco_total(self):
		return self.preco


class KitAtividade(ItemEvento):

	def __init__(self,descricao):
		self.descricao = descricao
		self.itens_evento = list()

	@property
	def preco_total(self):
		preco = 0.0

		for item_evento in self.itens_evento:
			preco += item_evento.preco_total

		return preco

	def add(self,item_evento):
		self.itens_evento.append(item_evento)

	def remove(self,item_evento):
		self.itens_evento.remove(item_evento)