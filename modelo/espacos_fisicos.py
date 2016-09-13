# -*- coding : utf-8 -*-

class EspacoSimples(EspacoFisico)
	
	def __init__(self,descricao,locatao,capacidade):
		delf.descricao = descricao
		self.lotacao = lotacao
		self.inscritos = list()

	@property
	def inscritos(self):
		return tuple(self._inscritos)

	def add_inscrito(self,participante):
		
		if len(self.inscritos) > self.lotacao:
			raise ValueError("Lotação máxima")

		self.inscritos.append(participante)

class EspacoComposto(EspacoFisico):

	def __init__(self,descricao):
		self.descricao
		self.espacos_satelites = list()

	@property
	def inscritos(self):
		pessoas = []

		for espaco in self.espacos_satelites:
			pessoas.append(espaco.inscritos)

		return tuple(pessoas)

	def add(self,espaco):
		self.espacos_satelites.append(espaco)

	def remover(self,espaco):
		self.espacos_satelites.remove(espaco)
