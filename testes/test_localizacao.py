# -*- coding: utf-8 -*-

import unittest
import sys,os

# Adicionando pasta externa para capturar os modelos
pasta_projeto = os.path.abspath("../")
sys.path.append(pasta_projeto)

from modelo.localizacao import Localizacao

class TestLocal(unittest.TestCase):

	def setUp(self):
		self.local = Localizacao("IFPI",1230,"Teresina","Piauí")

	def test_retorno_componentes_local(self):
		self.assertEqual(self.local.local,"IFPI")
		self.assertEqual(self.local.numero,1230)
		self.assertEqual(self.local.cidade,"Teresina")
		self.assertEqual(self.local.estado,"Piauí")
		

if __name__ == "__main__":
	unittest.main()