# -*- coding : utf-8 -*-

import sys,os

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

from abstracoes.descontos import *

class DescontosFactory(object):

	@staticmethod
	def obter(descricao):
		
		descontos = {
			"tutorial":  DescontoTutorial(),
			"geral":     DescontoGeral(),
			"hackathon": DescontoHackathon(),
			"palestra":  DescontoPalestra(),
			"workshop":  DescontoWorkshop(),
		}
	
		return descontos.get(descricao,DescontoNulo())