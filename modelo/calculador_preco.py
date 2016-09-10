# -*- coding : utf-8 -*-

class CalculadorPreco(object):

	def calcular_preco(self,inscricao,cupom_usado):

		valor_desconto = cupom_usado.obter_desconto(inscricao)

		preco_total = inscricao.preco_total

		preco_com_desconto = preco_total - valor_desconto
		
		return preco_com_desconto