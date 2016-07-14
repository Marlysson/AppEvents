# -*- coding: utf-8 -*-

import unittest
import sys,os

# Adicionando pasta externa para capturar os modelos
pasta_projeto = os.path.abspath("../")
sys.path.append(pasta_projeto)

from modelo.atividades import Tutorial , Minicurso , Palestra

class TestaTiposAtividades(unittest.TestCase):
	
	def setUp(self):
		self.tutorial   = Tutorial("Introdução a Python")
		self.mini_curso = Minicurso("Javascript Funcional")
		self.palestra   = Palestra("A Web com os Micro-Serviços")

	def testa_retorno_nome_atividade(self):
		self.assertEqual("Introdução a Python",self.tutorial.titulo)
		self.assertEqual("Javascript Funcional",self.mini_curso.titulo)
		self.assertEqual("A Web com os Micro-Serviços",self.palestra.titulo)

	def testa_tipo_atividade_usada(self):
		self.assertEqual("Tutorial",self.tutorial.tipo_evento)
		self.assertEqual("Palestra",self.palestra.tipo_evento)
		self.assertEqual("Mini-Curso",self.mini_curso.tipo_evento)

	def testa_retorno_preco_tipo_atividade(self):
		#Verificar se não é um teste redundante, já que o preço está sendo testado
		# no teste do enum do tipo da atividade
		self.assertEqual(10,self.tutorial.preco)
		self.assertEqual(50,self.palestra.preco)
		self.assertEqual(60,self.mini_curso.preco)


if __name__ == "__main__":
	unittest.main()