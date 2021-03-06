# -*- coding: utf-8 -*-

#Bibliotecas padrão
import unittest
import sys,os
from datetime import datetime, date, timedelta

# Adicionando pasta externa para capturar os modelos externos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

#Modelos
from modelo.evento import Evento
from modelo.inscricao import Inscricao
from modelo.atividades import AtividadeSimples
from modelo.pessoa import Pessoa
from modelo.cupom import Cupom
from modelo.compra import Compra
from modelo.espacos_fisicos import EspacoSimples

#Enums
from enums.tipo_sexo import TipoSexo
from enums.tipo_atividade import TipoAtividade

#Exceções
from abstracoes.exceptions import ValorPagoInferior
from abstracoes.exceptions import InscricaoJaPagaNaoAceitaItens
from abstracoes.exceptions import InscricaoJaPaga
from abstracoes.exceptions import CupomExpirado
from abstracoes.exceptions import CupomNaoEncontradoNoEvento

#Descontos
from abstracoes.descontos import DescontoTutorial , DescontoWorkshop , DescontoHackathon, DescontoGeral

from services.horario import Horario
from services.duracao import Duracao

class TestCompraInscricao(unittest.TestCase):

	def setUp(self):

		self.hoje = Horario()

		data_inicio = self.hoje.mais("1 dia")
		self.duracao_evento = Duracao(data_inicio,durando="3 dias")

		self.prazo_inscricoes = self.hoje.mais("1 dia")

		self.duracao1 = Duracao(data_inicio,durando="50 minutos")
		self.duracao2 = Duracao(self.duracao1.horario_final,durando="50 minutos")
		self.duracao3 = Duracao(self.duracao2.horario_final,durando="50 minutos")
		self.duracao4 = Duracao(self.duracao3.horario_final,durando="50 minutos")

		self.data_cupons = Horario()
		
		#Horario Atividades
		horario_tutorial     = self.duracao1
		horario_palestra     = self.duracao2
		horario_mesa_redonda = self.duracao3
		horario_workshop     = self.duracao4
		horario_hackathon    = Duracao(horario_workshop.inicio,durando="50 minutos")
		
		#Participante
		self.participante1 = Pessoa("Marlysson",18,TipoSexo.MASCULINO)
		self.participante2 = Pessoa("Marcos",25,TipoSexo.MASCULINO)
		
		#Salas
		self.sala1 = EspacoSimples("Sala-01",50,None)
		self.sala2 = EspacoSimples("Sala-02",50,None)
		self.sala3 = EspacoSimples("Sala-03",50,None)
		self.sala4 = EspacoSimples("Sala-04",50,None)
		self.sala5 = EspacoSimples("Sala-05",50,None)
		self.sala6 = EspacoSimples("Sala-06",50,None)

		#Atividades
		self.palestra     = AtividadeSimples(TipoAtividade.PALESTRA,"Lucrando com open-source",horario_palestra,0.0)
		self.tutorial     = AtividadeSimples(TipoAtividade.TUTORIAL,"Boas Práticas com Django",horario_tutorial,15.00)
		self.mesa_redonda = AtividadeSimples(TipoAtividade.MESA_REDONDA,"Pirataria na Web",horario_mesa_redonda,0.0)
		self.hackathon    = AtividadeSimples(TipoAtividade.HACKATHON,"Soluções Financeiras - Nubank",horario_hackathon,50.00)
		
		self.workshop1     = AtividadeSimples(TipoAtividade.WORKSHOP,"Python na Ciência",horario_workshop,30.00)
		self.workshop2     = AtividadeSimples(TipoAtividade.WORKSHOP,"Python no Ensino",horario_workshop,25.00)

		self.palestra.definir_espaco(self.sala1)
		self.tutorial.definir_espaco(self.sala2)
		self.mesa_redonda.definir_espaco(self.sala3)
		self.hackathon.definir_espaco(self.sala4)
		self.workshop1.definir_espaco(self.sala5)
		self.workshop2.definir_espaco(self.sala6)

		horarios_cupons = {
			"valido1" :   self.data_cupons.mais("1 dia"),
			"valido2" :   self.data_cupons.mais("1 dia"),
			"invalido1" : Horario("11/10/2015 16:00"),
			"invalido2":  Horario("20/1/2016 10:00")
		}

		self.cupom_geral = Cupom("LOTE_1",0.5,horarios_cupons.get("valido1"))
		self.cupom_geral.regra = DescontoGeral()

		self.cupom_tutorial = Cupom("TUTORIAIS_50",0.5,horarios_cupons.get("valido2"))
		self.cupom_tutorial.regra = DescontoTutorial()
		
		self.cupom_workshop = Cupom("WORKSHOP_10",0.1,horarios_cupons.get("invalido1"))
		self.cupom_workshop.regra = DescontoWorkshop()
		
		self.cupom_hackathon = Cupom("HACKATHON_50",0.5,horarios_cupons.get("invalido2"))
		self.cupom_hackathon.regra = DescontoHackathon()

		self.evento = Evento("Software Freedom Day","Descrição do Evento",self.duracao_evento)
		self.evento.prazo_inscricoes = self.prazo_inscricoes

		atividades = [self.palestra , self.tutorial , self.mesa_redonda , self.workshop1 , self.workshop2 , self.hackathon ]

		for atividade in atividades:
			self.evento.adicionar_atividade(atividade)

		cupons = [ self.cupom_geral , self.cupom_tutorial , self.cupom_workshop]
		
		for cupom in cupons:
			self.evento.adicionar_cupom(cupom)

	def test_inscricao_sem_itens_deve_ter_valor_zero(self):
		
		inscricao = Inscricao(self.participante1,self.evento)

		compra = Compra(inscricao)

		self.assertEqual(0,compra.preco_total)

	def test_valor_da_inscricao_e_o_valor_dos_seus_itens(self):
		
		inscricao = Inscricao(self.participante1,self.evento)

		inscricao.adicionar_atividade(self.workshop1)
		inscricao.adicionar_atividade(self.tutorial)

		compra = Compra(inscricao)

		valor_total = compra.preco_total

		self.assertEqual(45.00,valor_total)
	
	def test_ao_efetuar_compra_settar_inscricao_como_paga(self):
		
		inscricao = Inscricao(self.participante2,self.evento)

		inscricao.adicionar_atividade(self.tutorial)
		inscricao.adicionar_atividade(self.workshop1)

		compra = Compra(inscricao)
		compra.pagar(150.00)

		self.assertTrue(inscricao.paga)

	def test_deve_gerar_excecao_quando_pagar_uma_inscricao_ja_paga(self):

		inscricao = Inscricao(self.participante2,self.evento)

		inscricao.adicionar_atividade(self.tutorial)
		inscricao.adicionar_atividade(self.workshop1)

		compra = Compra(inscricao)
		compra.pagar(150.00)

		with self.assertRaises(InscricaoJaPaga):
			compra.pagar(100.00)
			
	def test_deve_retornar_data_de_pagamento_correta_ao_efetuar_compra(self):
		
		inscricao = Inscricao(self.participante2,self.evento)

		atividades = [ self.workshop1 , self.workshop2 , self.hackathon]

		for atividade in atividades:
			inscricao.adicionar_atividade(atividade)

		compra = Compra(inscricao)
		compra.aplicar_cupom(self.cupom_tutorial)

		self.assertEqual(105.00,compra.preco_total)

		compra.pagar(105.00)

		from datetime import datetime
		dia_pagamento = date.today()

		self.assertEqual(dia_pagamento,inscricao.data_pagamento)

	def test_nao_deve_aplicar_descontos_de_cupons_nao_ativos(self):
		
		inscricao = Inscricao(self.participante1,self.evento)

		atividades = [self.tutorial, self.workshop1 , self.workshop2 , self.hackathon]
		
		for atividade in atividades:
			inscricao.adicionar_atividade(atividade)

		compra = Compra(inscricao)

		with self.assertRaises(CupomExpirado):
			compra.aplicar_cupom(self.cupom_workshop)

	def test_deve_gerar_excecao_quando_aplicar_um_cupom_nao_cadastrado_no_evento(self):
		
		inscricao = Inscricao(self.participante2,self.evento)
		
		atividades = [self.tutorial, self.workshop1 , self.workshop2 , self.hackathon]
		
		for atividade in atividades:
			inscricao.adicionar_atividade(atividade)
		
		compra = Compra(inscricao)

		with self.assertRaises(CupomNaoEncontradoNoEvento):
			compra.aplicar_cupom(self.hackathon)

	def test_deve_gerar_excecao_ao_realizar_pagamento_inferior_ao_valor(self):

		inscricao = Inscricao(self.participante1,self.evento)

		inscricao.adicionar_atividade(self.tutorial)
		inscricao.adicionar_atividade(self.workshop1)

		compra = Compra(inscricao)

		with self.assertRaises(ValorPagoInferior):
			compra.pagar(40.00)
			
	def test_inscricao_paga_nao_deve_aceitar_novos_itens(self):

		inscricao = Inscricao(self.participante1,self.evento)

		inscricao.adicionar_atividade(self.tutorial)
		inscricao.adicionar_atividade(self.workshop1)

		compra = Compra(inscricao)
		compra.pagar(150.00)

		with self.assertRaises(InscricaoJaPagaNaoAceitaItens):
			inscricao.adicionar_atividade(self.hackathon)

	def test_compra_de_uma_inscricao_com_cupom_deve_retornar_valor_atualizado(self):
		
		inscricao = Inscricao(self.participante1,self.evento)

		atividades = [self.tutorial, self.workshop1 , self.workshop2 , self.hackathon]
		
		for atividade in atividades:
			inscricao.adicionar_atividade(atividade)

		compra = Compra(inscricao)
		compra.aplicar_cupom(self.cupom_tutorial) #Desconto de 50% nos tutoriais

		valor_compra = compra.preco_total

		self.assertEqual(112.5,valor_compra)

	def test_compra_deve_retornar_o_troco_correto_ao_participante(self):
		
		inscricao = Inscricao(self.participante1,self.evento)

		atividades = [self.tutorial, self.workshop1 , self.workshop2 , self.hackathon]
		
		for atividade in atividades:
			inscricao.adicionar_atividade(atividade)

		compra = Compra(inscricao)
		compra.aplicar_cupom(self.cupom_tutorial) #Cupom de 50% nos Tutoriais

		valor_compra = compra.preco_total

		compra.pagar(115.00)

		self.assertEqual(2.5,compra.troco)


if __name__ == "__main__":
	unittest.main(verbosity=2)