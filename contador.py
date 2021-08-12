class Contador:
	def pegar_numero():
		existe = False
		try:
			arq = open('id_atual.txt', 'r')
			arq.close()
			existe = True
		except:
			arq = open('id_atual.txt', 'w')
			arq.write('1')
			arq.close()
			existe = False
		if existe:
			arq = open('id_atual.txt', 'r')
			id_atual = int(arq.read()) + 1
			arq.close()
			return id_atual
		else:
			arq = open('id_atual.txt', 'r')
			id_atual = int(arq.read())
			arq.close()
			return id_atual