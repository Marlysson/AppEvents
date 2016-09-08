# -*- coding :utf-8 -*-

from enum import Enum

class TipoSexo(Enum):

	MASCULINO  = "Masculino"
	FEMININO   = "Feminino"
	OUTRO      = "Outro"

	def __repr__(self):
		return "{}".format(self.value)