# -*- coding : utf-8 -*-

import sys,os

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

from services.horario import Horario
from fabricas.descontos_factory import DescontosFactory

class Cupom(object):
	def __init__(self,descricao,desconto,validade,regra=None):
		
		self.descricao = descricao
		self.validade  = validade
		self.desconto  = desconto

		self.regra = DescontosFactory.obter(regra)

	@property
	def valido(self):

		hoje = Horario()

		if self.validade.data >= hoje.data:
			return True
		return False

	def obter_desconto(self,inscricao):
		
		preco_atividade = 0.0
	
		desconto = self.desconto * self.regra.obter_preco(inscricao)

		return desconto


	def __str__(self):
		return "<Cupom {} >".format(self.__dict__)