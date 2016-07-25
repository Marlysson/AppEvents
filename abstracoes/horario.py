# -*- coding: utf-8 -*-

class Horario(object):

	def __init__(self,string_data):
		self.data = string_data

	def nativo(self):
		from datetime import datetime

		datetime_convertido = datetime.strptime(self.data,"%d/%m/%Y %H:%M")

		ano = datetime_convertido.year
		mes = datetime_convertido.month
		dia = datetime_convertido.day
		hora = datetime_convertido.hour
		minuto = datetime_convertido.minute

		return datetime(ano,mes,dia,hora,minuto)

	def formatado(self):
		from datetime import datetime

		return datetime.strftime(self.nativo(),"%d/%m/%Y %H:%M")

	def __repr__(self):
		return "<Horario {}>".format(self.formatado())
