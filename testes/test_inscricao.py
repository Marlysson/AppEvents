# -*- coding: utf-8 -*-

import unittest
import sys,os
from datetime import datetime, timedelta

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

#Modelos
from modelo.atividade import Atividade
from modelo.evento import Evento
from modelo.pessoa import Pessoa
from modelo.inscricao import Inscricao

#Enums
from enums.tipo_atividade import TipoAtividade
from enums.status_evento import StatusEvento
from enums.tipo_sexo import TipoSexo

#Excecoes
from abstracoes.exceptions import AtividadeJaExisteNaInscricao
from abstracoes.exceptions import AtividadeNaoEncontradaNoEvento
from abstracoes.exceptions import InscricaoJaExisteNoEvento

class TestInscricao(unittest.TestCase):

	def setUp(self):

		self.hoje = datetime.now()

		data_inicio = self.hoje + timedelta(1)
		data_final  = data_inicio + timedelta(2)

		self.evento = Evento("Congresso de Profissionais Web","lorem ipsum....",data_inicio,data_final)
	
		self.palestra = Atividade(TipoAtividade.PALESTRA,"Introdução à Vuejs",datetime.now(),0.0)
		self.tutorial = Atividade(TipoAtividade.TUTORIAL,"Iniciando com Unittest",datetime.now(),15.00)
		self.mini_curso = Atividade(TipoAtividade.MINI_CURSO,"Python Avançado",datetime.now(),30.00)
		self.hackathon = Atividade(TipoAtividade.HACKATHON,"Hackeando Dados Públicos",datetime.now(),10.00)

		self.participante = Pessoa("Marlysson",20,TipoSexo.MASCULINO)
	
	def test_inscricao_recem_criada_deve_ter_zero_atividades(self):

		inscricao = Inscricao(self.participante,self.evento)

		self.assertEqual(0,len(inscricao.atividades))

	def test_deve_settar_automaticamente_em_inscricao_o_evento_adicionado(self):

		inscricao = Inscricao(self.participante,self.evento)

		self.assertEqual(inscricao.evento,self.evento)

	def test_deve_gerar_excecao_quando_se_inscrever_repetidamente_no_evento(self):

		with self.assertRaises(InscricaoJaExisteNoEvento):

			inscricao1 =  Inscricao(self.participante,self.evento)
			inscricao2 = Inscricao(self.participante,self.evento)

	def test_deve_gerar_excecao_ao_adicionar_atividade_repetida_na_inscricao(self):
		
		data_inicio = self.hoje + timedelta(1)
		data_final  = data_inicio + timedelta(2)

		evento = Evento("Congresso de Profissionais Web","lorem ipsum....",data_inicio,data_final)

		inscricao = Inscricao(self.participante,evento)

		for atividade in [self.palestra,self.hackathon]:
			evento.adicionar_atividade(atividade)	

		with self.assertRaises(AtividadeJaExisteNaInscricao):
			
			for atividade in [self.hackathon,self.palestra,self.hackathon]:
				inscricao.adicionar_atividade(atividade)
			
	def test_deve_gerar_excecao_adicionar_atividade_nao_associada_ao_evento_inscrito(self):

		data_inicio = self.hoje + timedelta(1)
		data_final  = data_inicio + timedelta(2)

		evento = Evento("Congresso de Profissionais Web","lorem ipsum....",data_inicio,data_final)
	
		for atividade in [self.palestra,self.hackathon,self.tutorial]:
			evento.adicionar_atividade(atividade)	

		inscricao = Inscricao(self.participante,evento)

		with self.assertRaises(AtividadeNaoEncontradaNoEvento):
			
			for atividade in [self.hackathon,self.mini_curso]:
				inscricao.adicionar_atividade(atividade)
			

	def test_deve_aceitar_adicionar_atividades_que_estejam_no_seu_evento(self):

		palestra = Atividade(TipoAtividade.PALESTRA,"CSS Escalável",datetime.now(),0.0)
		tutorial = Atividade(TipoAtividade.TUTORIAL,"Javascript e SVG",datetime.now(),15.00)
		mini_curso = Atividade(TipoAtividade.MINI_CURSO,"Javascript + StorageLocal",datetime.now(),30.00)
		hackathon = Atividade(TipoAtividade.HACKATHON,"Aplicações em NodeJS",datetime.now(),10.00)

		hoje = datetime.now()

		data_inicio = hoje + timedelta(1)
		data_final  = data_inicio + timedelta(2)

		evento = Evento("BrazilJS","lorem ipsum....",data_inicio,data_final)
		
		for atividade in [palestra,tutorial,mini_curso,hackathon]:
			evento.adicionar_atividade(atividade)

		participante = Pessoa("Marlysson",20,TipoSexo.MASCULINO)

		inscricao = Inscricao(participante,evento)
		
		for atividade in [palestra,hackathon,tutorial]:
			inscricao.adicionar_atividade(atividade)

	@unittest.skip("Não implementado")
	def test_deve_gerar_excecao_quando_ocorrer_uma_inscricao_fora_do_prazo(self):
		pass

if __name__ == "__main__":
	unittest.main()