# -*- coding : utf-8 -*-

class Atividade:

	def __init__(self,tipo,titulo,horario,preco=None):
		self.tipo = tipo
		self.titulo = titulo
		self.horario = horario
		self.preco = float(preco) if preco else 0
		
	def __repr__(self):
		return "<Atividade {} >".format(self.__dict__)