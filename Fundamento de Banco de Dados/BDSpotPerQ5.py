import pyodbc

conn = pyodbc.connect(r'DSN=mynewdsn;UID=user;PWD=password')
cursor = conn.cursor()

cursor.execute('use BDSpotPer')

while True:
	print("Questão 5\n")
	print("1) Exibir Albuns\n")
	print("2) Inserir Faixas na Playlist\n")

	sel = input("Digite a opção desejada\n")

	if sel == 1:
		cursor.execute('SELECT descrição FROM Albuns a')
		rows = cursor.fetchall()

		for row in rows:
			print(row.nome)
	elif sel == 2:
		playlist = input("Digite a Playlist desejada\n")
		album = input("Digite o nome do Album desejado\n")
		rawfaixa = input("Digite o numero das faixas que deseja inserir\n")
		faixas = rawfaixa.split(' ')

		cursor.execute("SELECT codPlay FROM Playlist WHERE nome = '?'", str(playlist),'y')
		codPlay = cursor.fetchval()

		cursor.execute("SELECT codAlbum FROM Album WHERE descrição = '?'", str(album),'y')
		codalbum = cursor.fetchval()

		cursor.execute("SELECT codfaixa, numFaixa FROM Faixa  WHERE codAlbum = '?'", str(codalbum),'y')
		faixasAlbum = cursor.fetchall()

		addFaixas = []

		for row in faixasAlbum:
			for faixa in faixas:
				if row.numFaixa == faixa:
					addFaixas.append(row.codfaixa)
		

		for codfaixa_f in addFaixas:
			cursor.execute('INSERT INTO FaixaPlaylist (codFaixa,codPlay) VALUES ( ? , ? )', int(codfaixa_f), int(codPlay))
			cursor.commit()
	else:
		print("opção invalida")