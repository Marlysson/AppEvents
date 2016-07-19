#-*- coding: utf-8 -*- 

import sys,os

#-*- coding : utf-8 -*-

#implementar uma classe de data/horario para calcular a diferença
from datetime import datetime , timedelta

class Atividade:
	def __init__(self,titulo):
		self.titulo = titulo
		self.horario = None
		self.ministrante = None
		self.tipo = str
		self.preco = float
		
	def __repr__(self):
		return "{} - {}".format(self.titulo,self.tipo)
