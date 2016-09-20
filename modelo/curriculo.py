# -*- coding :utf-8 -*-

class Curriculo(object):

	def __init__(self,linguagem,anos_experiência,empresa,descricao):
		self.linguagem        = linguagem
		self.anos_experiência = anos_experiência
		self.empresa          = empresa
		self.descricao        = descricao

	def __repr__(self):
		return "{}".format(self.__dict__)