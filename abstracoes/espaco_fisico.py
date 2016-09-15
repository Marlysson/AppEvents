# -*- coding : utf-8 -*-

from abc import ABCMeta , abstractproperty
from pprint import pformat

class EspacoFisico(metaclass=ABCMeta):

	@abstractproperty
	def inscritos(self):
		raise NotImplementedError("Property 'inscritos' não implementada")

	def add(self,espaco_fisico):
		raise TypeError("Tipo de espaço não suporta operação")

	def remover(self,espaco_fisico):
		raise TypeError("Tipo de espaço não suporta operação")

	def __repr__(self):
		return pformat(self.__dict__,indent=3)
		