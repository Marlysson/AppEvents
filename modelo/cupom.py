# -*- coding : utf-8 -*-

import sys,os
from datetime import date , timedelta

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

from abstracoes.descontos import DescontoNulo

class Cupom(object):
	def __init__(self,descricao,desconto,validade,regra=None):
		
		self.descricao = descricao
		self.validade  = validade
		self.desconto  = desconto

		self.regra = DescontoNulo()

	@property
	def valido(self):

		hoje = date.today()

		if self.validade >= hoje:
			return True
		return False


	def obter_desconto(self,inscricao):
		
		preco_atividade = 0.0
		
		for atividade in self.regra.obter_atividades(inscricao):
			preco_atividade += atividade.preco

		desconto = self.desconto * preco_atividade

		return desconto


	def __str__(self):
		return "<Cupom {} >".format(self.__dict__)