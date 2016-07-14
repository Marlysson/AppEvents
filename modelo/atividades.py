#-*- coding: utf-8 -*- 

import sys,os

# Adicionando pasta externa para capturar os modelos
pasta_projeto = os.path.abspath("../")
sys.path.append(pasta_projeto)

from abstracoes.atividade import Atividade
from enums.tipo_atividade import TipoAtividade

class Palestra(Atividade):
	def __init__(self,titulo):
		super().__init__(titulo)
		self.tipo = TipoAtividade.PALESTRA


class Minicurso(Atividade):
	def __init__(self,titulo):
		super().__init__(titulo)
		self.tipo = TipoAtividade.MINI_CURSO


class Tutorial(Atividade):
	def __init__(self,titulo):
		super().__init__(titulo)
		self.tipo = TipoAtividade.TUTORIAL	
