# -*- coding: utf-8

class Pessoa(object):
	def __init__(self,nome):
		self.nome = nome
		self.idade = int
		self.email = str
		self.cpf   = str
		self.tipo_perfil = str

	def __repr__(self):
		return "{}".format(self.nome)