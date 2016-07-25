# -*- coding: utf-8

from enum import Enum

class Status(Enum):
	
	ABERTO       = "Aberto"
	EM_ANDAMENTO = "Em Andamento"
	ENCERRADO    = "Encerrado"
	PENDENTE 	 = "Pendente"
	AGUARDANDO   = "Aguardando"

	def __str__(self):
		return "{}".format(self.value)