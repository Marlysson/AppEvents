# -*- coding: utf-8 -*-

import unittest
import sys,os
from datetime import datetime, timedelta

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

from modelo.evento import Evento
from modelo.inscricao import Inscricao

class TestCompraInscricao(unittest.TestCase):

	@unittest.skip("Não implementado")
	def test_compra_deve_ser_aprovada_com_sucesso(self):
		pass

	@unittest.skip("Não implementado")
	def test_ao_efetuar_compra_settar_inscricao_como_paga(self):
		pass

	@unittest.skip("Não implementado")
	def test_deve_gerar_excecao_quando_pagar_uma_inscricao_ja_paga(self):
		pass
		
	@unittest.skip("Não implementado")
	def test_deve_retornar_data_de_pagamento_correta_ao_efetuar_compra(self):
		pass

	@unittest.skip("Não implementado")
	def test_nao_deve_aplicar_descontos_de_cupons_nao_ativos(self):
		pass

	@unittest.skip("Não implementado")
	def test_valor_da_inscricao_e_o_valor_dos_seus_itens(self):
		pass

	@unittest.skip("Não implementado")
	def test_deve_gerar_excecao_ao_realizar_pagamento_inferior_ao_valor(self):
		pass


# pagamento = Pagamento(inscricao,usuario)
# pagamento.efetuar_pagamento(valor)

# compra = Compra(inscricao,usuario)
# compra.pagar(valor)


if __name__ == "__main__":
	unittest.main(verbosity=2)