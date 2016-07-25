# -*- coding: utf-8

from enum import Enum

class TipoParticipante(Enum):
	
	PARTICIPANTE  = "Participante"
	ORGANIZADOR   = "Organizador"
	PALESTRANTE   = "Palestrante"

	def __str__(self):
		return "{}".format(self.value)