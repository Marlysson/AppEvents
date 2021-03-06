# -*- coding : utf-8 -*- 

import sys , os

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

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
	def com_horas(self):
	    return datetime(self.ano,self.mes,self.dia,self.hora,self.minuto,0)

	@property
	def data(self):
		return date(self.ano,self.mes,self.dia)
	
	def mais(self,horario_adicional):

		quantidade,recorrencia = horario_adicional.split(" ")

		factory = FactoryRecorrencia.criar(self,recorrencia)
		
		hora_somada = factory.somar(int(quantidade))

		dados = {
			"dia" : hora_somada.day ,
			"mes": hora_somada.month ,
			"ano": hora_somada.year ,
			"hora": hora_somada.hour ,
			"minuto": hora_somada.minute
		}

		formatada = "{}/{}/{} {}:{}".format(dados["dia"],dados["mes"],dados["ano"],dados["hora"],dados["minuto"])
		
		return Horario(formatada)
		
	def __repr__(self):
		
		return "{}/{}/{} {}:{}".format(
				self.dia,
				self.mes,
				self.ano,
				self.hora,
				self.minuto
		)