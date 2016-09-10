
'''
	Classe para representar as exceções que podem ocorrer na aplicação
'''

# Exceções para Evento

class AtividadeJaExisteNoEvento(ValueError):
	pass

class EventoDataInvalida(ValueError):
	pass

class InscricaoJaExisteNoEvento(ValueError):
	pass

# Exceptions de Atividade

class AtividadeJaExisteNaInscricao(ValueError):
	pass

class AtividadeNaoEncontradaNoEvento(ValueError):
	pass


# Exceções para Inscricao

class PeriodoInvalidoParaInscricoes(ValueError):
	pass

class InscricaoJaPagaNaoAceitaInscricoes(ValueError):
	pass


# Exceções para Compra de Inscrição

class ValorPagoInferior(ValueError):
	pass

class InscricaoJaPaga(Exception):
	pass

class CupomNaoEncontradoNoEvento(Exception):
	pass

class CupomExpirado(Exception):
	pass