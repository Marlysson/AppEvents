# -*- coding: utf-8 -*-

import unittest
import sys,os

# Adicionando pasta externa para capturar os modelos
pasta_projeto = os.path.abspath("../")
sys.path.append(pasta_projeto)

from enums.tipo_status import Status
from enums.tipo_atividade import TipoAtividade
from enums.tipo_usuario import TipoParticipante

class TestEnums(unittest.TestCase):

	def setUp(self):
		self.aberto    = Status.ABERTO
		self.andamento = Status.EM_ANDAMENTO
		self.encerrado = Status.ENCERRADO
		
		self.participante = TipoParticipante.PARTICIPANTE
		self.organizador  = TipoParticipante.ORGANIZADOR
		self.palestrante  = TipoParticipante.PALESTRANTE

		self.palestra   = TipoAtividade.PALESTRA
		self.mini_curso = TipoAtividade.MINI_CURSO
		self.tutorial   = TipoAtividade.TUTORIAL

	def test_retorno_enum_tipo_status(self):
		self.assertEqual("Aberto",str(self.aberto))
		self.assertEqual("Em Andamento",str(self.andamento))
		self.assertEqual("Encerrado",str(self.encerrado))

	def test_retorno_enum_tipo_usuario_evento(self):
		self.assertEqual("Participante",str(self.participante))
		self.assertEqual("Organizador",str(self.organizador))
		self.assertEqual("Palestrante",str(self.palestrante))

	def test_retorno_enum_tipo_atividade(self):
		self.assertEqual("Palestra",str(self.palestra.nome))
		self.assertEqual("Tutorial",str(self.tutorial.nome))
		self.assertEqual("Mini-Curso",str(self.mini_curso.nome))

	def test_retorno_preco_atividade(self):
		self.assertEqual(50,self.palestra.preco)
		self.assertEqual(10,self.tutorial.preco)
		self.assertEqual(60,self.mini_curso.preco)

if __name__ == "__main__":
	unittest.main()