# -*- coding : utf-8 -*-

class Local(object):
	def __init__(self,rua,bairro,numero,cidade):
		self.rua  = rua
		self.bairro = bairro
		self.numero = numero
		self.cidade = cidade

	def __repr__(self):
		return "{}".format(self.__dict__)