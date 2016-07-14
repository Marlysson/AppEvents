# -*- coding : utf-8 -*-

class Localizacao(object):
	def __init__(self,local,numero,cidade,estado):
		self.local   = local
		self.numero = numero
		self.cidade = cidade
		self.estado = estado

	def __repr__(self):
		return "{}, nº {}, {}-{}".format(self.local,self.numero,self.cidade,self.estado)