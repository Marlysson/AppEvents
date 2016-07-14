# -*- coding: utf-8

from enum import Enum

class TipoAtividade(Enum):
	PALESTRA     = ("Palestra",50)
	TUTORIAL     = ("Tutorial",10)
	MINI_CURSO   = ("Mini-Curso",60)

	def __init__(self,nome,preco):
		self.nome = nome
		self.preco = float(preco)

	def __str__(self):
		return "{}({:.2f})".format(self.nome,self.preco)
