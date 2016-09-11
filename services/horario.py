# -*- coding : utf-8 -*- 

from datetime import datetime , date , timedelta
from fabricas.recorrencia_factory import FactoryRecorrencia

class Horario(object):

	def __init__(self,string_horario = None):
				
		if string_horario == None:
			horario = datetime.now()
			self.horario = "{}/{}/{} {}:{}".format(horario.day,horario.month,horario.year,horario.hour,horario.minute)
		else:
			self.horario = string_horario

		self.dia = None
		self.mes = None
		self.ano = None

		self.hora = None
		self.minuto = None

		self.validar()

	def validar(self):

		try:

			data, hora = self.horario.split(" ")

			self.dia,self.mes,self.ano = [int(i) for i in data.split("/")]

			self.hora,self.minuto = [int(i) for i in hora.split(":")]

			horario = datetime(
				self.ano,
				self.mes,
				self.dia,
				self.hora,
				self.minuto,
			)

		except Exception:
			raise ValueError("Horário Inválido")

	@property
	def datetime(self):
	    return datetime(self.ano,self.mes,self.dia,self.hora,self.minuto)

	@property
	def date(self):
		return date(self.ano,self.mes,self.dia)
	
	def mais(self,horario_adicional):

		quantidade,recorrencia = horario_adicional.split(" ")

		factory = FactoryRecorrencia.criar(self,recorrencia)

		return factory.somar(int(quantidade))

	def __repr__(self):
		
		return "{}/{}/{} {}:{}".format(
				self.dia,
				self.mes,
				self.ano,
				self.hora,
				self.minuto
		)