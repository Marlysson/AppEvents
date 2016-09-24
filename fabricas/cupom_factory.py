# -*- coding : utf-8 -*-

import sys,os

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

from modelo.cupom import Cupom
from fabricas.descontos_factory import DescontosFactory

class CupomFactory(object):

	@staticmethod
	def obter(descricao,porcentagem,validade,regra=None):
		
		regra = DescontosFactory.obter(regra)
		
		return Cupom(descricao,porcentagem,validade,regra)