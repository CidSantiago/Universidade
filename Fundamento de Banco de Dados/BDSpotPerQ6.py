import pyodbc
import datetime

conn = pyodbc.connect(r'DSN=mynewdsn;UID=user;PWD=password')
cursor = conn.cursor()

cursor.execute('use BDSpotPer')
sel = 0

while True:
	print("Questão 6\n")
	descAlbum = input("Digite a descrição do Album desejado")

	codAlbum = cursor.execute("SELECT codAlbum FROM album WHERE descrição = '%?%'", str(descAlbum)).fetchval()

	while sel != -1:
		print("1) Alterar Gravadora\n")
		print("2) Alterar Descrição\n")
		print("3) Alterar Preço de Compra\n")
		print("4) Alterar Data da Compra\n")
		print("5) Alterar Data da Gravação\n")
		print("6) Alterar Tipo da Compra\n")
		print("7) Trocar o Album a ser alterado\n")

		sel = input("Digite a opção desejada:\n")

		if sel == 1:
			newGravNome = input("Digite o nome da gravadora desejada\n")
			newGravCod = cursor.execute("SELECT codGrav FROM Gravadora WHERE nome = '?'", str(newGravNome))

			cursor.execute("UPDATE Album SET codGrav = ? WHERE codAlbum = ?", int(newGravCod), int(codAlbum))
			cursor.commit()

		elif sel == 2:
			newDesc = input("Digite a nova Descrição\n")

			cursor.execute("UPDATE Album SET Descrição = '?'WHERE codAlbum = ?", str(newDesc), int(codAlbum))
			cursor.commit()

		elif sel == 3:
			newPrecoCompra = input("Digite o novo Preço de Compra\n")

			cursor.execute("UPDATE Album SET preçoCompra = ? WHERE codAlbum = ?", float(newPrecoCompra) , int(codAlbum)) #procurar função decimal em python
			cursor.commit()

		elif sel == 4:
			newData = input("Digite a nova Data de Compra (AAAA/MM/DD)\n")
			newData = newData.split('/')

			cursor.execute("UPDATE Album SET dataCompra = ? WHERE codAlbum = ?", datetime.date(newData[0],newData[1],newData[2]), int(codAlbum))
			cursor.commit()

		elif sel == 5:
			newData = input("Digite a nova Data de Gravação (AAAA/MM/DD)\n")
			newData = newData.split('/')

			cursor.execute("UPDATE Album SET dataGravação = ? WHERE codAlbum = ?", datetime.date(newData[0],newData[1],newData[2]), int(codAlbum))
			cursor.commit()						
		
		elif sel == 6:
			newTipo = input("Deseje o Tipo desejado (ADD ou DDD)\n")

			cursor.execute("UPDATE Album SET tipoCompra = '?' WHERE codAlbum = ?", str(newTipo), int(codAlbum))
			cursor.commit()						
			
		elif sel == 7:
			sel = -1	

		else:
			print("opção invalida")
