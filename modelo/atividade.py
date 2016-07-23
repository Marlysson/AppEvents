
class Atividade:

	'''
		>>> atividade = Atividade("Palestra","Iniciando Vue.js",40.00)
		>>> print atividade
		Iniciando Vue.js - Palestra
	'''

	def __init__(self,tipo,titulo,preco=None):
		self.tipo = tipo
		self.titulo = titulo
		self.horario = None

		if not preco:
			self.preco = 0
		else:
			self.preco = preco
			
		
	def __repr__(self):
		return "{} - {}".format(self.titulo,self.tipo)
