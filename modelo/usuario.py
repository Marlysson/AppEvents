# -*- coding : utf-8 -*-

class Usuario(object):
	
	'''
		:email  str
		:senha  str
		:pessoa Pessoa
	'''

	def __init__(self):
		self.email = email
		self.senha = senha
		self.pessoa = pessoa
		self.estado = None
		self.eventos_participados = list()
		
	def criar_evento(self,evento):
		pass