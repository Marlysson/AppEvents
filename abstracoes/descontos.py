# -*- coding : utf-8 -*-

import sys,os

# # Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

from modelo.atividade import Atividade
from abc import ABCMeta , abstractmethod

class Desconto(metaclass=ABCMeta):

	@abstractmethod
	def obter_atividades(inscricao):
		raise ValueError("Método 'obter_atividades' não implementada")


class DescontoHackathon(Desconto):

	def obter_atividades(self,inscricao):
	    
	    tipo_atividade = lambda atividade : atividade.tipo.value == "Hackathon"

	    atividades = filter(tipo_atividade,inscricao.atividades)

	    return atividades

class DescontoWorkshop(Desconto):

	def obter_atividades(self,inscricao):
	    
	    tipo_atividade = lambda atividade : atividade.tipo.value == "Workshop"

	    atividades = filter(tipo_atividade,inscricao.atividades)

	    return atividades
	
class DescontoTutorial(Desconto):

	def obter_atividades(self,inscricao):

	    tipo_atividade = lambda atividade : atividade.tipo.value == "Tutorial"

	    atividades = filter(tipo_atividade,inscricao.atividades)

	    return atividades

class DescontoGeral(Desconto):

	def obter_atividades(self,inscricao):
	    return inscricao.atividades
		
class DescontoNulo(Desconto):

	def obter_atividades(self,inscricao):

		from datetime import datetime

		return [ Atividade("Padrão","Padrão",datetime.now(),0.0) ]