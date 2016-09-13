# -*- coding : utf-8 -*-

import sys , os
from datetime import date , timedelta

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

from modelo.cupom import Cupom
from modelo.calculador_preco import CalculadorPreco

from abstracoes.exceptions import InscricaoJaPaga
from abstracoes.exceptions import ValorPagoInferior

from abstracoes.exceptions import CupomNaoEncontradoNoEvento
from abstracoes.exceptions import CupomExpirado

from abstracoes.descontos import DescontoNulo


class Compra(object):

	def __init__(self,inscricao):
		
		self.calculador = CalculadorPreco()
		self.inscricao = inscricao

		self.troco = 0.0

		validade = date.today() + timedelta(days=1)
		cupom_nulo = Cupom("CupomNulo",0.0,validade,DescontoNulo)
	
		self.cupom = cupom_nulo

	@property
	def preco_total(self):
		valor_a_pagar = self.calculador.calcular_preco(self.inscricao,self.cupom)

		return valor_a_pagar

	def pagar(self,valor_pago):

		if self.inscricao.paga:
			raise InscricaoJaPaga("Não pode pagar novamente esta inscrição")

		if valor_pago < self.preco_total:
			raise ValorPagoInferior("Valor inválido")

		self.confirmar_inscricao(self.inscricao)

		self.troco = valor_pago - self.preco_total

	def confirmar_inscricao(self,inscricao):

		inscricao.paga = True
		inscricao.data_pagamento = date.today()

		evento = inscricao.evento
		evento.adicionar_inscricao(self.inscricao)

		for atividade in inscricao.atividades:
			
			espaco_fisico = atividade.espaco

			espaco_fisico.add_inscrito(inscricao.participante)

			atividade.add_inscrito(inscricao.participante)


	def aplicar_cupom(self,cupom):

		if cupom not in self.inscricao.cupons_evento:
			raise CupomNaoEncontradoNoEvento("Não encontrado cupom associado ao evento")

		if not cupom.valido:
			raise CupomExpirado("Cupom Expirado")

		self.cupom = cupom