#-*- coding: utf-8 -*- 

class Atividade:
	def __init__(self,titulo):
		self.titulo = titulo
		self.horario = None
		self.ministrante = None
		self.tipo = str
		self.preco = float
		
	def __repr__(self):
		return "{} - {}".format(self.titulo,self.tipo)
