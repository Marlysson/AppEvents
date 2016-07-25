# -*- coding: utf-8

from enum import Enum

class TipoAtividade(Enum):
	
	PALESTRA     = "Palestra"
	TUTORIAL     = "Tutorial"
	MINI_CURSO   = "Mini-Curso"

	def __str__(self):
		return "{}".format(self.value)
