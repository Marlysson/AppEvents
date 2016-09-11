# -*- coding : utf-8 -*-

import sys , os

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

from services.horario import Horario
from abstracoes.exceptions import DuracaoDeTempoInvalida

class Duracao(object):

	def __init__(self,horario,durando=None):
		self.inicio = horario
		self.final = self.inicio.mais(durando)

		self.validar()

	def validar(self):

		if (self.inicio.com_horas - self.final.com_horas).seconds == 0:
			raise DuracaoDeTempoInvalida("Duração Inválida")

	def __repr__(self):
		return "{} até {}".format(self.inicio,self.final)