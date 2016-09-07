# -*- coding: utf-8 -*-

import unittest

class TestCompraInscricao(unittest.TestCase):

	@unittest.skip("Não implementado")
	def test_compra_deve_ser_aprovada_com_sucesso(self):


	@unittest.skip("Não implementado")
	def test_ao_efetuar_compra_settar_inscricao_como_paga(self):


	@unittest.skip("Não implementado")
	def test_deve_gerar_excecao_quando_pagar_uma_inscricao_ja_paga(self):

		
	@unittest.skip("Não implementado")
	def test_deve_retornar_data_de_pagamento_correta_ao_efetuar_compra(self):






# pagamento = Pagamento(inscricao,usuario)
# pagamento.efetuar_pagamento(valor)

# compra = Compra(inscricao,usuario)
# compra.pagar(valor)


if __name__ == "__main__":
	unittest.main(verbosity=2)