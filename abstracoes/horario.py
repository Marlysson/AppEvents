# -*- coding : utf-8 -*- 

from datetime import datetime , date

class Horario(object):

	def __init__(self,string_horario):
		
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
		
		# quantidade,recorrencia = horario_adicional.split(" ")

		# if recorrencia == "dias":

		# elif recorrencia == "meses":

		# elif recorrencia == "anos":

		# elif recorrencia == "horas":

		# elif recorrencia == "minutos"
		pass

	def menos(self,horario_a_menos):	
		pass

	def __repr__(self):
		
		return "{}/{}/{} {}:{}".format(
				self.dia,
				self.mes,
				self.ano,
				self.hora,
				self.minuto
		)