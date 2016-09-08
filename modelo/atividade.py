# -*- coding : utf-8 -*-

class Atividade:

	'''
		Representa uma atividade qualquer dentro do evento

		:tipo: string
		:titulo: string
		:horario: datetime
		:preco: float

		tutorial = Atividade(TipoAtividade.TUTORIAL , 'Iniciando com Python' , datetime(2016,12,05,15,0,0) , 15.00)

	'''
	def __init__(self,tipo,titulo,horario,preco=None):
		self.tipo = tipo
		self.titulo = titulo
		self.horario = horario
		self.preco = float(preco) if preco else 0
	
	def __eq__(self,atividade):
		
		if self.titulo = atividade.titulo:
			return True
		return False


	def __repr__(self):
		return "<Atividade {} >".format(self.__dict__)