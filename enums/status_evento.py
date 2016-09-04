# -*- coding: utf-8

from enum import Enum

class StatusEvento(Enum):
	
	#Visibilidade Evento
	NAO_PUBLICADO = "Não Publicado"
	PUBLICADO     = "Publicado"

	#Ocorrência do Evento
	NAO_INICIADO  = "Não Iniciado"
	EM_ANDAMENTO  = "Em Andamento"
	ENCERRADO     = "Encerrado"

	def __repr__(self):
		return "{}".format(self.value)