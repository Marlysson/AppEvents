# -*- coding -*- utf-8

import sys,os

# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)

from abstracoes.observer import Observer

class Logger(Observer):

	def __init__(self,arquivo):
		self.arquivo = arquivo

	def update(self,mensagem):
		with open(self.arquivo,'a') as arquivo:
			arquivo.write(mensagem+"\n")

