# -*- coding: utf-8

from enum import Enum

class TipoAtividade(Enum):
	
	PALESTRA     = "Palestra"
	TUTORIAL     = "Tutorial"
	MINI_CURSO   = "Mini Curso"
	MESA_REDONDA = "Mesa Redonda"
	WORKSHOP     = "Workshop"
	HACKATHON    = "Hackathon"
	COFFEE_BREAK = "Coffee Break"

	def __str__(self):
		return "{}".format(self.value)
