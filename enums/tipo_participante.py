# -*- coding: utf-8

from enum import Enum

class TipoParticipante(Enum):
	
	ESTUDANTE     = "Estudante"
	PROFISSIONAL  = "Profissional"
	ORGANIZADOR   = "Organizador"
	PALESTRANTE   = "Palestrante"
	
	def __str__(self):
		return "{}".format(self.value)