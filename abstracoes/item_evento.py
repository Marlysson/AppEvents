# -*- coding : utf-8 -*-

from abc import ABCMeta , abstractmethod , abstractproperty

class ItemEvento(metaclass=ABCMeta):

	@abstractproperty
	def preco_total(self):
		raise NotImplementedError("Property 'preco_total' não implementada")

	def add(self,atividade):
		raise TypeError("Operação não permitida")

	def remover(self,atividade):
		raise TypeError("Operação não permitida")

	def __repr__(self):
		return "{}".format(self.descricao)