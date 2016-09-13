# -*- coding : utf-8 -*-

from abc import ABCMeta , abstractproperty

class EspacoFisico(metaclass=ABCMeta):

	@abstractproperty
	def inscritos(self):
		raise NotImplementedError("Property 'inscritos' não implementada")
	
	@abstractmethod
	def add_inscrito(self):
		raise TypeError("Tipo de espaço não suporta operação")
		
	def add(self,espaco_fisico):
		raise TypeError("Tipo de espaço não suporta operação")

	def remover(self,espaco_fisico):
		raise TypeError("Tipo de espaço não suporta operação")