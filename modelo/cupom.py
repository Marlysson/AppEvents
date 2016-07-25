# -*- coding : utf-8 -*-

#Base de Cupom

class Cupom(object):
	def __init__(self,descricao,desconto,validade):
		self.descricao = descricao
		self.desconto  = desconto
		self.validade  = validade

	def valido(self):
		from datetime import date
		hoje = date.today()

		return self.validade <= hoje

	def descontar(Compra):
		pass

	def __str__(self):
		return "<Cupom {} ({})>".format(self.descricao,self.validade)
