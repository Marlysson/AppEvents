# -*- coding: utf-8

from enum import Enum

class Status(Enum):
	ABERTO       = "Aberto"
	EM_ANDAMENTO = "Em andamento"
	ENCERRADO    = "Encerrado"

	def __str__(self):
		return "{}".format(self.value)