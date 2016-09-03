# -*- coding : utf-8 -*-

#Base de Cupom

import sys,os
from datetime import date

class Cupom(object):
	def __init__(self,descricao,desconto,validade):
		self.descricao = descricao
		self.desconto  = desconto
		self.validade  = validade
		self.regra_desconto = None

	def validar(self):
		from datetime import date

		hoje = date.today()
		
		return hoje <= self.validade

	def __str__(self):
		return "<Cupom {} ({})>".format(self.descricao,self.validade)
