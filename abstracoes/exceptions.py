
'''
	Classe para representar as exceções que podem ocorrer na aplicação
'''

# Exceções para Evento

class AtividadeJaExisteNoEvento(ValueError):
	pass

class EventoDataInvalida(ValueError):
	pass


# Exceções para Inscricao

class AtividadeJaExisteNaInscricao(ValueError):
	pass

class AtividadeNaoEncontradaNoEvento(ValueError):
	pass

class InscricaoJaExisteNoEvento(ValueError):
	pass

class PeriodoInvalidoParaInscricoes(ValueError):
	pass

# Exceções para Compra de Incrição


