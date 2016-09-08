# -*- coding : utf-8 -*-

#Base de Cupom

import sys,os
from datetime import date

class Cupom(object):
	def __init__(self,descricao,desconto,validade):
		self.descricao = descricao
		self.desconto  = desconto
		self.validade  = validade
		self.promocao = None

	def __eq__(self,cupom):
		
		if self.__dict__ == cupom.__dict__:
			return True
		return False

	def validar(self):
		from datetime import date

		hoje = date.today()
		
		if hoje <= self.validade:
			return True
		else:
			return False
		
	def __str__(self):
		return "<Cupom {} ({})>".format(self.descricao,self.validade)
