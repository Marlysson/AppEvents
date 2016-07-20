# -*- coding : utf-8 -*-

class Localizacao(object):
	def __init__(self,local,cidade,estado):
		self.local  = local
		self.cidade = cidade
		self.estado = estado

	def __repr__(self):
		return "{}, {}-{}".format(self.local,self.cidade,self.estado)