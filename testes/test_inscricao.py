# -*- coding: utf-8 -*-

import unittest
import sys,os
from datetime import datetime, timedelta

import pdb

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

		evento.adicionar_atividade(self.palestra)
		evento.adicionar_atividade(self.hackathon)

		with self.assertRaises(AtividadeJaExisteNaInscricao):
			
			inscricao.adicionar_atividade(self.hackathon)
			inscricao.adicionar_atividade(self.palestra)
			inscricao.adicionar_atividade(self.hackathon)

	def test_deve_gerar_excecao_adicionar_atividade_nao_associada_ao_evento_inscrito(self):

		data_inicio = self.hoje + timedelta(1)
		data_final  = data_inicio + timedelta(2)

		evento = Evento("Congresso de Profissionais Web","lorem ipsum....",data_inicio,data_final)
	
		evento.adicionar_atividade(self.palestra)
		evento.adicionar_atividade(self.hackathon)
		evento.adicionar_atividade(self.tutorial)

		inscricao = Inscricao(self.participante,evento)

		with self.assertRaises(AtividadeNaoEncontradaNoEvento):

			inscricao.adicionar_atividade(self.hackathon)
			inscricao.adicionar_atividade(self.mini_curso)


if __name__ == "__main__":
	unittest.main()