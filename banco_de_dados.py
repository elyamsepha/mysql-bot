import mysql.connector
from tabulate import tabulate

banco = mysql.connector.connect(
	host="localhost",
	user="usuario(possivelmente root)",
	passwd="",
	database="nome do banco de dados"
)

cursor = banco.cursor(buffered=True)



class Cadastro:
	def adicionar_usuario(nome, id_discord, id_usuario, data):
		cursor.execute(f"INSERT INTO cadastrados (nome,id_discord,id,data_de_cadastro) VALUES ('{nome}','{id_discord}','{id_usuario}','{data}')")

	def verificar_usuario(id_discord):
		cursor.execute(f"SELECT * FROM cadastrados WHERE id_discord='{id_discord}'")
		if cursor.rowcount == 1:
			return True
		if cursor.rowcount == 0:
			return False
class Mostrar:
	def info(metodo,info):
		metodo = metodo.replace(':','')
		try:
			cursor.execute(f"SELECT * FROM cadastrados WHERE {metodo}='{info}'")
		except:
			return f"método de reconhecimento '{metodo}' não existe"
		if cursor.rowcount == 1:
			retorno = cursor.fetchall()
			retorno = tabulate(retorno, headers=['nome', 'id_discord', 'id',' data_de_cadastro'], tablefmt='psql')
			return retorno
		if cursor.rowcount == 0:
			return f"não existe um usuario cadastrado com este {metodo}"
	def todos():
		cursor.execute(f"SELECT * FROM cadastrados")
		retorno = cursor.fetchall()
		retorno = tabulate(retorno, headers=['nome', 'id_discord', 'id',' data_de_cadastro'], tablefmt='psql')
		arq = open('todos_cadastrados.txt','w')
		arq.write(retorno)
		arq.close()