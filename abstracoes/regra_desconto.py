
class RegraDesconto:
	def obter_desconto(self,inscricao):
		pass

class DescontoAtividade(RegraDesconto):

	def __init__(self,tipo_atividade):
		self.atividade = tipo_atividade

	def obter_desconto(self,inscricao):

		tipo_atividade = []
		preco_total = 0.0
		desconto = 0.0

		for atividade in inscricao.atividades:
			if atividade.tipo.lower() == self.atividade.lower():
				tipo_atividade.append(atividade)

		for atividade in tipo_atividade:
			preco_total += atividade.preco

		desconto = self.desconto * preco_total

		return desconto

class DescontoGeral(RegraDesconto):

	def obter_desconto(inscricao):
		preco_total = 0.0

		for atividade in inscricao.atividades:
			preco_total += atividade.preco

		return preco_total * desconto
