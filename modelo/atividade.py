
class Atividade:

	'''
		>>> atividade = Atividade("Palestra","Iniciando Vue.js",40.00)
		>>> print atividade
		Iniciando Vue.js - Palestra
	'''

	def __init__(self,tipo,titulo,preco):
		self.tipo = tipo
		self.titulo = titulo
		self.preco = preco
		self.horario = None
		
	def __repr__(self):
		return "{} - {}".format(self.titulo,self.tipo)
