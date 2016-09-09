# -*- coding: utf-8 -*-

import unittest
import sys,os
from datetime import datetime, timedelta

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

#Modelos
from modelo.evento import Evento
from modelo.inscricao import Inscricao
from modelo.atividade import Atividade
from modelo.pessoa import Pessoa

#Enums
from enums.tipo_sexo import TipoSexo
from enums.tipo_atividade import TipoAtividade

from abstracoes.regra_desconto import DescontoAtividade

class TestCompraInscricao(unittest.TestCase):

	def setUp(self):

		hoje = datetime.now()

		self.participante = Pessoa("Marcos",18,TipoSexo.MASCULINO)

		horario_tutorial = datetime.now() + timedelta(1)

		horario_palestra = hoje + timedelta(days=1,minutes=40)

		inicio_evento = hoje + timedelta(1)
		final_evento = inicio_evento + timedelta(1)

		self.palestra = Atividade(TipoAtividade.PALESTRA,"Lucrando com open-source",horario_palestra,0.0)
		self.tutorial = Atividade(TipoAtividade.TUTORIAL,"Boas Práticas com Django",horario_tutorial,15.00)

		cupom1 = Cupom("MINICURSO_30",0.3,self.hoje - timedelta(1))
		cupom1.promocao = DescontoAtividade(TipoAtividade.TUTORIAL)

		self.evento = Evento("Software Freedom Day","Descrição do Evento",inicio_evento,final_evento)
		
		self.evento.adicionar_atividade(self.palestra)
		self.evento.adicionar_atividade(self.tutorial)
		
	@unittest.skip("Não implementado")
	def test_nao_deve_aplicar_descontos_de_cupons_nao_ativos(self):
		pass

	@unittest.skip("Não implementado")
	def test_valor_total_das_inscricoes_e_o_valor_total_dos_seus_items(self):
		pass

	# @unittest.skip("Não implementado")
	def test_inscricao_sem_itens_deve_ter_valor_zero(self):
		
		inscricao = Inscricao(self.participante,self.evento)

		self.assertEqual(0,inscricao.preco_total)

	@unittest.skip("Não implementado")
	def test_ao_efetuar_compra_settar_inscricao_como_paga(self):
		
		inscricao = Inscricao(participante,evento)

		inscricao.adicionar_atividade(tutorial)

		compra = Compra(inscricao)

		compra.pagar(150.00)

	@unittest.skip("Não implementado")
	def test_deve_gerar_excecao_quando_pagar_uma_inscricao_ja_paga(self):
		pass
		
	@unittest.skip("Não implementado")
	def test_deve_retornar_data_de_pagamento_correta_ao_efetuar_compra(self):
		pass

	@unittest.skip("Não implementado")
	def test_nao_deve_aplicar_descontos_de_cupons_nao_ativos(self):
		
		inscricao = Inscricao(participante,evento)

		inscricao.adicionar_atividade(tutorial)

		compra = Compra(inscricao)
		# compra.adicionar_cupom(Cupom)

		calculador = CalculadorDePreco(compra)

		valor_a_pagar =	calculador.preco_total()

		compra.pagar(100)

	@unittest.skip("Não implementado")
	def test_valor_da_inscricao_e_o_valor_dos_seus_itens(self):
		pass

	@unittest.skip("Não implementado")
	def test_deve_gerar_excecao_ao_realizar_pagamento_inferior_ao_valor(self):
		pass

	@unittest.skip("Não implementado")
	def test_inscricao_paga_nao_deve_aceitar_novos_itens(self):
		pass


# pagamento = Pagamento(inscricao,usuario)
# pagamento.efetuar_pagamento(valor)

# compra = Compra(inscricao,usuario)
# compra.pagar(valor)


if __name__ == "__main__":
	unittest.main(verbosity=2)