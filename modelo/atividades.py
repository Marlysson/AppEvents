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

		self.espaco = None
		self.inscritos = list()

		self.ministrantes = list()

	@property
	def horario_inicio(self):
		return self.duracao.inicio

	@property
	def horario_final(self):
		return self.duracao.final

	@property
	def preco_total(self):
		return self.preco

	def definir_espaco(self,espaco):

		self.espaco = espaco
		espaco.atividade = self

	def add_inscrito(self,participante):
		if len(self.inscritos) == self.espaco.capacidade:
			raise ValueError("Capacidade máxima do espaço atingida")

		self.inscritos.append(participante)

	def add_responsavel(self,responsavel):
		self.ministrantes.append(responsavel)

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