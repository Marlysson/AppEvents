# -*- coding: utf-8 -*-

class Horario(object):


	'''
	>>> horario = Horario("25/07/2016 16:00")
	>>> hora = horario.hora
	>>> data = horario.data
	>>> print(hora)
	16:00
	>>> print(data)
	25/07/2016
	'''

	def __init__(self,string_data):
		self.string_data = string_data


	@property
	def data(self):
		return "{:%d/%m/%Y}".format(self.__nativo())

	@property
	def hora(self):
		return "{:%H:%M}".format(self.__nativo())


	def __nativo(self):
		from datetime import datetime

		datetime_convertido = datetime.strptime(self.string_data,"%d/%m/%Y %H:%M")

		ano = datetime_convertido.year
		mes = datetime_convertido.month
		dia = datetime_convertido.day
		hora = datetime_convertido.hour
		minuto = datetime_convertido.minute

		return datetime(ano,mes,dia,hora,minuto)

	def __formatado(self):
		from datetime import datetime

		return datetime.strftime(self.__nativo(),"%d/%m/%Y %H:%M")

	def __repr__(self):
		return "<Horario {}>".format(self.__formatado())

