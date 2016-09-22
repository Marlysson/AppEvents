# -*- coding : utf-8 -*-

from abc import ABCMeta , abstractmethod

class Desconto(metaclass=ABCMeta):

	@abstractmethod
	def obter_preco(inscricao):
		raise NotImplementedError("Método 'obter_preco' não implementada")


class DescontoHackathon(Desconto):

	def obter_preco(self,inscricao):
	    
	    tipo_atividade = lambda atividade : atividade.tipo.value == "Hackathon"

	    atividades = filter(tipo_atividade,inscricao.atividades)

	    return sum([atividade.preco for atividade in atividades])

class DescontoWorkshop(Desconto):

	def obter_preco(self,inscricao):
	    
	    tipo_atividade = lambda atividade : atividade.tipo.value == "Workshop"

	    atividades = filter(tipo_atividade,inscricao.atividades)

	    return sum([atividade.preco for atividade in atividades])
	
class DescontoTutorial(Desconto):

	def obter_preco(self,inscricao):

	    tipo_atividade = lambda atividade : atividade.tipo.value == "Tutorial"

	    atividades = filter(tipo_atividade,inscricao.atividades)

	    return sum([atividade.preco for atividade in atividades])

class DescontoGeral(Desconto):

	def obter_preco(self,inscricao):
	    return sum([atividade.preco for atividade in inscricao.atividades])
		
class DescontoNulo(Desconto):

	def obter_preco(self,inscricao):
		return 0.0