# -*- coding: utf-8 -*-

#Bibliotecas padrão
import unittest
import sys,os

# Adicionando pasta externa para capturar os modelos externos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

from modelo.atividades import AtividadeSimples
from modelo.espacos_fisicos import EspacoSimples
from modelo.curriculo import Curriculo
from modelo.pessoa import Pessoa

from enums.tipo_atividade import TipoAtividade
from enums.tipo_sexo import TipoSexo

from services.horario import Horario
from services.duracao import Duracao

class TestResponsavel(unittest.TestCase):

	def setUp(self):
		self.hoje = Horario()

		data_inicio = self.hoje.mais("1 dia")
		self.duracao1 = Duracao(data_inicio,durando="50 minutos")

		self.espaco = EspacoSimples("SALA-01",40,None)

		self.palestra = AtividadeSimples(TipoAtividade.PALESTRA,"Introdução à Vuejs",self.duracao1,0.0)
		self.palestra.definir_espaco(self.espaco)

	def test_deve_retornar_responsavel_da_atividade(self):
		
		marlysson = Pessoa("Marlysson",20,TipoSexo.MASCULINO)
		marcelo = Pessoa("Marcelo",22,TipoSexo.MASCULINO)

		self.palestra.add_responsavel(marlysson)
		self.palestra.add_responsavel(marcelo)

		self.assertListEqual(self.palestra.ministrantes,[marlysson,marcelo])

	def test_deve_retornar_curriculo_do_responsavel_atividade(self):

		pessoa = Pessoa("Luciano Ramalho",50,TipoSexo.MASCULINO)
		curriculo = Curriculo("Python",15,"Thougthworks","")

		pessoa.add_curriculo(curriculo)

		self.palestra.add_responsavel(pessoa)

		self.assertEqual(self.palestra.ministrantes[0],pessoa)

	if __name__ == "__main__":
		unittest.main(verbosity=2)
