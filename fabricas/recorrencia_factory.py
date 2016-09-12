# -*- coding : utf-8 -*-

import os , sys
from datetime import date , timedelta

from abc import ABCMeta , abstractmethod


# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)


class FactoryRecorrencia(object):

	@staticmethod
	def criar(horario,string):
		
		if string.lower() in ["hora","horas"]:
			return SomadorHora(horario)

		elif string.lower() in ["dias" , "dia"]:
			return SomadorDia(horario)

		elif string.lower() in ["minutos" , "minuto"]:
			return SomadorMinutos(horario)

		elif string.lower() in ["segundos" , "segundo"]:
			return SomadorSegundos(horario)

class SomadorRecorrencia(metaclass=ABCMeta):

	def __init__(self,horario):
		self.horario = horario

	@abstractmethod
	def somar(self,quantidade):
		raise NotImplementedError("Método 'somar' não implementado")

class SomadorHora(SomadorRecorrencia):

	def somar(self,quantidade):
		self.horario = self.horario.com_horas + timedelta(hours=quantidade)

		return self.horario

class SomadorDia(SomadorRecorrencia):

	def somar(self,quantidade):

		self.horario = self.horario.com_horas + timedelta(days=quantidade)

		return self.horario

class SomadorMinutos(SomadorRecorrencia):

	def somar(self,quantidade):
		self.horario = self.horario.com_horas + timedelta(minutes=quantidade)

		return self.horario


class SomadorSegundos(SomadorRecorrencia):

	def somar(self,quantidade):
		self.horario = self.horario.com_horas + timedelta(seconds=quantidade)

		return self.horario