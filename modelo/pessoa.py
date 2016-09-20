# -*- coding: utf-8

class Pessoa(object):
	def __init__(self,nome,idade,genero):
		self.nome = nome
		self.idade = idade
		self.genero = genero
		self.curriculo = None

	def add_curriculo(self,curriculo):
		self.curriculo = curriculo

	def __repr__(self):
		return "<Pessoa {} >".format(self.__dict__)
