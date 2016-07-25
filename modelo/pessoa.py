# -*- coding: utf-8

class Pessoa(object):
	def __init__(self,nome,idade,genero):
		self.nome = nome
		self.idade = idade
		self.genero = genero

	def __repr__(self):
		return "<Pessoa {} >".format(self.__dict__)
