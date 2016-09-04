# -*- coding :utf-8 -*-

from enum import Enum

class StatusCompra(Enum):

	RECUSADO   = "Recusada"
	APROVADA   = "Aprovada"

	def __repr__(self):
		return "{}".format(self.value)