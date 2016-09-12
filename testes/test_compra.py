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

#Enums
from enums.tipo_sexo import TipoSexo
from enums.tipo_atividade import TipoAtividade

#Exceções
from abstracoes.exceptions import ValorPagoInferior
from abstracoes.exceptions import InscricaoJaPagaNaoAceitaInscricoes
from abstracoes.exceptions import InscricaoJaPaga
from abstracoes.exceptions import CupomExpirado
from abstracoes.exceptions import CupomNaoEncontradoNoEvento

#Descontos
from abstracoes.descontos import DescontoTutorial , DescontoWorkshop , DescontoHackathon, DescontoGeral

class TestCompraInscricao(unittest.TestCase):

	def setUp(self):

		self.hoje = datetime.now()
		self.data_cupons = date.today()

		inicio_evento = self.hoje + timedelta(days=1)
		final_evento = inicio_evento + timedelta(days=2)
		
		#Horario Atividades
		horario_tutorial = inicio_evento + timedelta(minutes=10)	
		horario_palestra = horario_tutorial + timedelta(minutes=30)
		horario_mesa_redonda = horario_palestra + timedelta(minutes=30)
		horario_workshop = horario_mesa_redonda + timedelta(minutes=60)
		horario_hackathon = horario_workshop + timedelta(minutes=60)
		
		#Participante
		self.participante1 = Pessoa("Marlysson",18,TipoSexo.MASCULINO)
		self.participante2 = Pessoa("Marcos",25,TipoSexo.MASCULINO)

		#Atividades
		self.palestra     = AtividadeSimples(TipoAtividade.PALESTRA,"Lucrando com open-source",horario_palestra,0.0)
		self.tutorial     = AtividadeSimples(TipoAtividade.TUTORIAL,"Boas Práticas com Django",horario_tutorial,15.00)
		self.mesa_redonda = AtividadeSimples(TipoAtividade.MESA_REDONDA,"Pirataria na Web",horario_mesa_redonda,0.0)
		self.hackathon    = AtividadeSimples(TipoAtividade.HACKATHON,"Soluções Financeiras - Nubank",horario_hackathon,50.00)
		
		self.workshop1     = AtividadeSimples(TipoAtividade.WORKSHOP,"Python na Ciência",horario_workshop,30.00)
		self.workshop2     = AtividadeSimples(TipoAtividade.WORKSHOP,"Python no Ensino",horario_workshop,25.00)

		horarios_cupons = {
			"valido1" :   self.data_cupons + timedelta(days=1),
			"valido2" :   self.data_cupons + timedelta(days=1),
			"invalido1" : self.data_cupons - timedelta(days=2),
			"invalido2":  self.data_cupons - timedelta(days=2)
		}

		self.cupom_geral = Cupom("LOTE_1",0.5,horarios_cupons.get("valido1"))
		self.cupom_geral.regra = DescontoGeral()

		self.cupom_tutorial = Cupom("TUTORIAIS_50",0.5,horarios_cupons.get("valido2"))
		self.cupom_tutorial.regra = DescontoTutorial()
		
		self.cupom_workshop = Cupom("WORKSHOP_10",0.1,horarios_cupons.get("invalido1"))
		self.cupom_workshop.regra = DescontoWorkshop()
		
		self.cupom_hackathon = Cupom("HACKATHON_50",0.5,horarios_cupons.get("invalido2"))
		self.cupom_hackathon.regra = DescontoHackathon()

		self.evento = Evento("Software Freedom Day","Descrição do Evento",inicio_evento,final_evento)
		self.evento.prazo_inscricoes = date.today() + timedelta(days=3)

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

		inscricao1 = Inscricao(self.participante2,self.evento)

		inscricao1.adicionar_atividade(self.tutorial)
		inscricao1.adicionar_atividade(self.workshop1)

		compra1 = Compra(inscricao1)
		compra1.pagar(150.00)

		compra2 = Compra(inscricao1)

		with self.assertRaises(InscricaoJaPaga):
			compra2.pagar(100.00)
			

	def test_deve_retornar_data_de_pagamento_correta_ao_efetuar_compra(self):
		
		inscricao = Inscricao(self.participante2,self.evento)

		atividades = [ self.workshop1 , self.workshop2 , self.hackathon]

		for atividade in atividades:
			inscricao.adicionar_atividade(atividade)

		compra = Compra(inscricao)
		compra.aplicar_cupom(self.cupom_tutorial)

		self.assertEqual(105.00,compra.preco_total)

		compra.pagar(105.00)

		self.assertEqual(0.0,compra.troco)

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

		with self.assertRaises(InscricaoJaPagaNaoAceitaInscricoes):
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


	def test_compra_deve_descontar_metade_do_preco_da_inscricao_e_retornar_troco_correto(self):

		inscricao = Inscricao(self.participante1,self.evento)

		atividades = [self.tutorial, self.workshop1 , self.workshop2 , self.hackathon]
		
		for atividade in atividades:
			inscricao.adicionar_atividade(atividade)

		compra = Compra(inscricao)

		self.assertEqual(120.00,compra.preco_total)

		compra.aplicar_cupom(self.cupom_geral) #Cupom 50% de desconto Geral

		valor_com_cupom = compra.preco_total

		self.assertEqual(60.00,valor_com_cupom)

		compra.pagar(100.00)

		self.assertEqual(40.00,compra.troco)


if __name__ == "__main__":
	unittest.main(verbosity=2)