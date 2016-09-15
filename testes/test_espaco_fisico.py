# -*- coding : utf-8 -*-

import unittest
import sys,os

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

from modelo.espacos_fisicos import EspacoSimples , EspacoComposto
from modelo.localizacao import Local

class TestEspacoFisico(unittest.TestCase):

	def setUp(self):
		self.local = Local("Praça da Liberdade","Centro",1597,"Teresina - PI")

		self.predio = EspacoComposto("Prédio A",self.local)
		
		self.andar_b1 = EspacoComposto("Primeiro Andar",self.predio)
		self.andar_b2 = EspacoComposto("Segundo Andar",self.predio)

		self.sala1 = EspacoSimples("Sala B1-01",40,self.predio)
		self.sala2 = EspacoSimples("Sala B2-01",40,self.predio)

		self.auditorio = EspacoSimples("Auditório A2",150,self.predio)

	def test_espaco_fisico_deve_retornar_sua_capacidade(self):
		
		self.assertEqual(self.sala1.capacidade,40)

	def test_deve_adicionar_corretamente_espaco_fisico_em_outro_maior(self):
		
		self.andar_b1.add(self.sala1)
		self.andar_b2.add(self.sala2)

		self.predio.add(self.andar_b1)
		self.predio.add(self.andar_b2)

	def test_deve_gerar_excecao_quando_adicionar_um_espaco_fisico_maior_em_um_simples(self):
		
		with self.assertRaises(TypeError):
			self.sala2.add(self.auditorio)

	def test_deve_adicionar_diversos_tipos_de_espacos_fisicos_ao_geral_retornando_lotacao(self):

		self.andar_b1.add(self.sala1)
		self.andar_b2.add(self.sala2)

		self.predio.add(self.andar_b1)
		self.predio.add(self.andar_b2)

		self.assertEqual(80,self.predio.capacidade)

		self.predio.add(self.auditorio)

		self.assertEqual(230,self.predio.capacidade)

if __name__ == "__main__":
	unittest.main(verbosity=2)