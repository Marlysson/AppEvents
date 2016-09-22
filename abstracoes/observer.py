# -*- coding : utf-8 -*-

from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):

	@abstractmethod
	def update(self,dado):
		raise NotImplementedError("Método 'update' não implementado")


class Subject(metaclass=ABCMeta):

	@abstractmethod
	def registrar(self,observer):
		raise NotImplementedError("Método 'registrar' não implementado")		

	@abstractmethod
	def remover(self,observer):
		raise NotImplementedError("Método 'remover' não implementado")

	@abstractmethod
	def notificar(self):
		raise NotImplementedError("Método 'notificar' não implementado")