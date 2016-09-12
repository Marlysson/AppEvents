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

	@property
	def horario_inicio(self):
		return self.inicio

	@property
	def horario_final(self):
		return self.final

	def validar(self):

		if self.final.com_horas <= self.inicio.com_horas:
			raise DuracaoDeTempoInvalida("Duração Inválida")

	def __repr__(self):
		return "{} até {}".format(self.inicio,self.final)