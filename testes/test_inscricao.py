# -*- coding: utf-8 -*-

import unittest
import sys,os
from datetime import datetime, date , timedelta

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

#Modelos
from modelo.atividades import AtividadeSimples
from modelo.evento import Evento
from modelo.pessoa import Pessoa
from modelo.inscricao import Inscricao
from modelo.compra import Compra
from modelo.espacos_fisicos import EspacoSimples

#Enums
from enums.tipo_atividade import TipoAtividade
from enums.status_evento import StatusEvento
from enums.tipo_sexo import TipoSexo

#Excecoes
from abstracoes.exceptions import AtividadeJaExisteNaInscricao
from abstracoes.exceptions import AtividadeNaoEncontradaNoEvento
from abstracoes.exceptions import InscricaoJaExisteNoEvento
from abstracoes.exceptions import PeriodoInvalidoParaInscricoes
from abstracoes.exceptions import InscricaoNaoExisteNoEvento

#Services
from services.horario import Horario
from services.duracao import Duracao


class TestInscricao(unittest.TestCase):
	
	def setUp(self):

		self.hoje = Horario()

		data_inicio = self.hoje.mais("1 dia")
		self.duracao = Duracao(data_inicio,durando="3 dias")

		self.prazo_inscricoes = self.hoje.mais("10 dias")

		self.evento = Evento("Congresso de Profissionais Web","lorem ipsum....",self.duracao)
		self.evento.prazo_inscricoes = self.prazo_inscricoes

		self.duracao1 = Duracao(data_inicio,durando="50 minutos")
		self.duracao2 = Duracao(self.duracao1.horario_final,durando="50 minutos")
		self.duracao3 = Duracao(self.duracao2.horario_final,durando="50 minutos")
		self.duracao4 = Duracao(self.duracao3.horario_final,durando="50 minutos")

		#Salas
		self.sala1 = EspacoSimples("Sala-01",50,None)
		self.sala2 = EspacoSimples("Sala-02",50,None)
		self.sala3 = EspacoSimples("Sala-03",50,None)
		self.sala4 = EspacoSimples("Sala-04",50,None)

		self.palestra = AtividadeSimples(TipoAtividade.PALESTRA,"Introdução à Vuejs",self.duracao1,0.0)
		self.tutorial = AtividadeSimples(TipoAtividade.TUTORIAL,"Iniciando com Unittest",self.duracao2,15.00)
		self.mini_curso = AtividadeSimples(TipoAtividade.MINI_CURSO,"Python Avançado",self.duracao3,30.00)
		self.hackathon = AtividadeSimples(TipoAtividade.HACKATHON,"Hackeando Dados Públicos",self.duracao4,10.00)

		self.palestra.definir_espaco(self.sala1)
		self.tutorial.definir_espaco(self.sala2)
		self.mini_curso.definir_espaco(self.sala3)
		self.hackathon.definir_espaco(self.sala4)

		self.participante = Pessoa("Marlysson",20,TipoSexo.MASCULINO)
	
	def test_inscricao_recem_criada_deve_ter_zero_atividades(self):

		inscricao = Inscricao(self.participante,self.evento)

		self.assertEqual(0,len(inscricao.atividades))
	
	def test_deve_settar_automaticamente_em_inscricao_o_evento_adicionado(self):

		inscricao = Inscricao(self.participante,self.evento)

		self.assertEqual(inscricao.evento,self.evento)
	
	def test_deve_gerar_excecao_quando_se_inscrever_repetidamente_no_evento(self):

		inscricao1 =  Inscricao(self.participante,self.evento)
		inscricao2 =  Inscricao(self.participante,self.evento)

		compra = Compra(inscricao1)
		compra.pagar(10)

		with self.assertRaises(InscricaoJaExisteNoEvento):
			compra = Compra(inscricao2)
			compra.pagar(10)
	
	def test_deve_gerar_excecao_ao_adicionar_atividade_repetida_na_inscricao(self):
		
		inscricao = Inscricao(self.participante,self.evento)

		for atividade in [self.palestra,self.hackathon]:
			self.evento.adicionar_atividade(atividade)	

		with self.assertRaises(AtividadeJaExisteNaInscricao):
			
			for atividade in [self.hackathon,self.palestra,self.hackathon]:
				inscricao.adicionar_atividade(atividade)
	
	def test_deve_gerar_excecao_adicionar_atividade_nao_associada_ao_evento_inscrito(self):

		for atividade in [self.palestra,self.hackathon,self.tutorial]:
			self.evento.adicionar_atividade(atividade)	

		inscricao = Inscricao(self.participante,self.evento)

		with self.assertRaises(AtividadeNaoEncontradaNoEvento):
			
			for atividade in [self.hackathon,self.mini_curso]:
				inscricao.adicionar_atividade(atividade)
			
	def test_deve_aceitar_adicionar_atividades_que_estejam_no_seu_evento(self):

		palestra = AtividadeSimples(TipoAtividade.PALESTRA,"CSS Escalável",self.duracao1,0.0)
		tutorial = AtividadeSimples(TipoAtividade.TUTORIAL,"Javascript e SVG",self.duracao2,15.00)
		mini_curso = AtividadeSimples(TipoAtividade.MINI_CURSO,"Javascript + StorageLocal",self.duracao3,30.00)
		hackathon = AtividadeSimples(TipoAtividade.HACKATHON,"Aplicações em NodeJS",self.duracao4,10.00)

		for atividade in [palestra,tutorial,mini_curso,hackathon]:
			self.evento.adicionar_atividade(atividade)

		inscricao = Inscricao(self.participante,self.evento)
		
		for atividade in [palestra,hackathon,tutorial]:
			inscricao.adicionar_atividade(atividade)
	
	@unittest.skip("Não implementado")
	def test_deve_gerar_excecao_quando_ocorrer_uma_inscricao_fora_do_prazo(self):
		
		from unittest.mock import Mock

		data_inicio = self.hoje + timedelta(days=1)
		data_final  = data_inicio + timedelta(days=3)


		evento = Evento("Congresso de Profissionais Web","lorem ipsum....",data_inicio,data_final)
		evento.prazo_inscricoes = (data_inicio + timedelta(days=2)).date()

		evento.apto_inscricoes = Mock(return_value=False)

		evento.adicionar_atividade(self.tutorial)
		evento.adicionar_atividade(self.palestra)

		with self.assertRaises(PeriodoInvalidoParaInscricoes):
			inscricao = Inscricao(self.participante,evento)

	def test_deve_retornar_data_do_checkin_da_inscricao(self):
		
		for atividade in [self.palestra,self.tutorial,self.mini_curso,self.hackathon]:
			self.evento.adicionar_atividade(atividade)

		inscricao = Inscricao(self.participante,self.evento)
		
		for atividade in [self.palestra,self.hackathon,self.tutorial]:
			inscricao.adicionar_atividade(atividade)

		compra = Compra(inscricao)
		compra.pagar(25.00)

		inscricao.realizar_checkin()

		from datetime import date

		hoje = date.today()

		self.assertEqual(inscricao.data_checkin,hoje)

	def test_deve_gerar_excecao_de_checkin_de_inscricao_nao_encontrada_no_evento(self):
		
		for atividade in [self.palestra,self.tutorial,self.mini_curso,self.hackathon]:
			self.evento.adicionar_atividade(atividade)

		inscricao = Inscricao(self.participante,self.evento)
		
		for atividade in [self.palestra,self.hackathon,self.tutorial]:
			inscricao.adicionar_atividade(atividade)

		with self.assertRaises(InscricaoNaoExisteNoEvento):
			inscricao.realizar_checkin()
		

	def test_inscricao_unica_deve_adicionar_todas_as_atividades_do_evento_inscrito(self):
		
		self.evento.inscricao_unica = True

		tutorial = AtividadeSimples(TipoAtividade.TUTORIAL,"Javascript e SVG",self.duracao2,15.00)
		mini_curso = AtividadeSimples(TipoAtividade.MINI_CURSO,"Javascript + StorageLocal",self.duracao3,30.00)
		hackathon = AtividadeSimples(TipoAtividade.HACKATHON,"Aplicações em NodeJS",self.duracao4,10.00)

		for atividade in [tutorial,mini_curso,hackathon]:
			self.evento.adicionar_atividade(atividade)

		inscricao = Inscricao(self.participante,self.evento)
		
		self.assertListEqual(inscricao.atividades,[tutorial,mini_curso,hackathon])

if __name__ == "__main__":
	unittest.main(verbosity=2)