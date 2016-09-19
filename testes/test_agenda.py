# -*- coding : utf-8 -*-

import unittest
import sys,os

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

from modelo.evento import Evento
from modelo.atividades import AtividadeSimples
from modelo.pessoa import Pessoa
from modelo.localizacao import Local
from modelo.espacos_fisicos import EspacoSimples , EspacoComposto

from enums.tipo_sexo import TipoSexo
from enums.tipo_atividade import TipoAtividade

from services.horario import Horario
from services.duracao import Duracao

class AgendaEvento(unittest.TestCase):

	def setUp(self):

		self.local = Local("Av. Frei Serafim","Centro",1010,"Teresina-Pi")
		
		self.hoje = Horario()

		data_inicio = self.hoje.mais("1 dia")
		self.duracao_evento = Duracao(data_inicio,durando="3 dias")

		self.prazo_inscricoes = self.hoje.mais("1 dia")

		self.duracao1 = Duracao(data_inicio,durando="50 minutos")
		self.duracao2 = Duracao(self.duracao1.horario_final,durando="50 minutos")
		self.duracao3 = Duracao(self.duracao2.horario_final,durando="50 minutos")
		self.duracao4 = Duracao(self.duracao3.horario_final,durando="50 minutos")

		#Horario Atividades
		horario_tutorial     = self.duracao1
		horario_palestra     = self.duracao2
		horario_mesa_redonda = self.duracao3
		horario_workshop     = self.duracao4
		horario_hackathon    = Duracao(self.duracao4.inicio,durando="50 minutos")
		
		#Atividades
		self.palestra     = AtividadeSimples(TipoAtividade.PALESTRA,"Lucrando com open-source",horario_palestra,0.0)
		self.tutorial     = AtividadeSimples(TipoAtividade.TUTORIAL,"Boas Práticas com Django",horario_tutorial,15.00)
		self.mesa_redonda = AtividadeSimples(TipoAtividade.MESA_REDONDA,"Pirataria na Web",horario_mesa_redonda,0.0)
		self.hackathon    = AtividadeSimples(TipoAtividade.HACKATHON,"Soluções Financeiras - Nubank",horario_hackathon,50.00)
		
		self.predio_B = EspacoComposto("Prédio B",self.local)

		self.andar_1 = EspacoComposto("B1",self.local)
		self.andar_2 = EspacoComposto("B2",self.local)

		self.salas = [ EspacoSimples("B"+str(num+1)+"-01",40,self.local) for num in range(1,5)]

		self.andar_1.add(self.salas[0])
		self.andar_1.add(self.salas[1])
		self.andar_2.add(self.salas[2])
		self.andar_2.add(self.salas[3])

		self.predio_B.add(self.andar_1)
		self.predio_B.add(self.andar_2)

		self.evento = Evento("Software Freedom Day","Descrição do Evento",self.duracao_evento)
		self.evento.prazo_inscricoes = self.prazo_inscricoes

		# self.evento.add(self.andar_1)
		# self.evento.add(self.andar_2)
		atividades = [self.palestra , self.tutorial , self.mesa_redonda , self.hackathon ]

		for atividade in zip(atividades:
			self.evento.adicionar_atividade(atividade)

	def test_deve_retornar_lista_de_atividades_ordenada_do_espaco_fisico(self):
			
		agenda = self.andar_1.gerar_agenda()
		print(agenda)

	def test_deve_retornar_lista_de_atividades_ordenada_do_evento(self):
		pass

if __name__ == "__main__":
	unittest.main(verbosity=2)