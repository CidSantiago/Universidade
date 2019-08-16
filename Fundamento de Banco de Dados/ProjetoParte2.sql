-- Questão 1 --

create database BDSpotPer
on
    primary
	(
	NAME = 'BDSpotPer',
	FILENAME = 'C:\BD\BDSpotPer.mdf',
	SIZE = 10240KB,
	FILEGROWTH = 5120KB
	),

	FILEGROUP BDSpotPerFG1
	(
	NAME = 'BDSpotPer11',
	FILENAME = 'C:\BD\BDSpotPer11.ndf',
	SIZE = 2048KB,
	FILEGROWTH = 50%
	),
	(
	NAME = 'BDSpotPer12',
	FILENAME = 'C:\BD\BDSpotPer12.ndf',
	SIZE = 2048KB,
	FILEGROWTH = 50%
	),

	FILEGROUP BDSpotPerFG2
	(
	NAME = 'BDSpotPer21',
	FILENAME = 'C:\BD\BDSpotPer21.ndf',
	SIZE = 2048KB,
	FILEGROWTH = 50%
	)

	LOG ON
	(
	NAME = 'BDSpotPerLog',
	FILENAME = 'C:\BD\BDSpotPerLog.ldf',
	SIZE = 2048KB,
	FILEGROWTH = 20%
	);

	use BDSpotPer;

-- Questão 2 --

	Create Table Gravadora
	(
	    codGrav int not null,
		nome char(50) not null,
		endereço char(50) not null,
		site char(50) not null,
		
		CONSTRAINT PK_Gravadora PRIMARY KEY(codGrav)
	) on BDSpotPerFG1

	Create Table Telefones
	(
	    codGrav int not null,
		telefone char(20) not null,

		CONSTRAINT PK_Telefones PRIMARY KEY(codGrav, telefone),
		CONSTRAINT FK_TelefonesGravadora FOREIGN KEY(codGrav) REFERENCES Gravadora(codGrav),
		CONSTRAINT UN_Telefones UNIQUE(telefone)
	) on BDSpotPerFG1

	Create Table Album
	(
	    codAlbum int not null,
		codGrav int not null,
		descrição char(50) not null,
		preçoCompra decimal(6,2) not null,
		dataCompra datetime,
		dataGravação datetime,
		tipoCompra char(8),

		CONSTRAINT PK_Album PRIMARY KEY(codAlbum),
		CONSTRAINT FK_AlbumGravadora FOREIGN KEY(codGrav) REFERENCES Gravadora(codGrav),
		CONSTRAINT CK_dataCompra CHECK(dataGravação > '2000-01-01 00:00:00.000'),
		CONSTRAINT CK_tipoCompra CHECK(tipoCompra = 'Fisica' OR tipoCompra = 'Download')
	) on BDSpotPerFG1

	Create Table Interprete
	(
	    codInt int not null,
		nome char(50) not null,
		tipo char(50) not null,

		CONSTRAINT PK_Interprete PRIMARY KEY(codInt)
	) on BDSpotPerFG1

	Create Table Composição
	(
	    codComposição int not null,
		descrição char(50) not null,

		CONSTRAINT PK_Composição PRIMARY KEY(codComposição)
	) on BDSpotPerFG1
	
	Create Table PeriodoMusical
	(
	    codPer int not null,
		descrição char(50) not null,
		tempoAtivo char(50) not null,

		CONSTRAINT PK_PeriodoMusical PRIMARY KEY(codPer)
	) on BDSpotPerFG1

	Create Table Compositor
	(
	    codCompositor int not null,
		codPer int not null,
		nome char(50) not null,
		localNascimento char(50) not null,
		dtNascimento datetime,
		dtMor datetime,

		CONSTRAINT PK_Compositor PRIMARY KEY(codCompositor),
		CONSTRAINT FK_CompositorPeriodo FOREIGN KEY(codPer) REFERENCES PeriodoMusical(codPer)
	) on BDSpotPerFG1
	
	Create Table Playlist
	(
		codPlay int not null,
		nome char(50) not null,
		dataCriação datetime not null,
		tempoTotalExec int,

		CONSTRAINT PK_Playlist PRIMARY KEY(codPlay)
	) on BDSpotPerFG2

	Create Table infoPlaylist
	(
		codPlay int not null,
		codFaixa int not null,
		vezesTocado int not null,
		ultimaTocado datetime not null,

		CONSTRAINT PK_infoPlaylist PRIMARY KEY(codPlay,codFaixa),
		CONSTRAINT FK_infoPlaylistPlaylist FOREIGN KEY(codPlay) REFERENCES Playlist(codPlay)
	) on BDSpotPerFG2

	Create Table Faixa
	(
	    codFaixa int not null,
		codAlbum int not null,
		codInt int not null,
		codComposição int not null,
		descrição char(50) not null,
		tipoGravação char(3) not null,
		numFaixa int not null,
		tempoExec int not null,

		CONSTRAINT PK_Faixa PRIMARY KEY(codFaixa),
		CONSTRAINT FK_FaixaAlbum FOREIGN KEY(codAlbum) REFERENCES Album(codAlbum)
		ON update cascade ON delete cascade, --Questao 4, item C
		CONSTRAINT FK_FaixaInterprete FOREIGN KEY(codInt) REFERENCES Interprete(codInt),
		CONSTRAINT FK_FaixaComposição FOREIGN KEY(codComposição) REFERENCES Composição(codComposição),
		CONSTRAINT CK_tipoGravação CHECK(tipoGravação = 'ADD' OR tipoGravação = 'DDD')
	) on BDSpotPerFG2
	
	Create Table FaixaCompositor
	(
	    codFaixa int not null,
	    codCompositor int not null,

		CONSTRAINT PK_FaixaCompositor PRIMARY KEY(codFaixa, codCompositor),
		CONSTRAINT FK_FaixaCompositorFaixa FOREIGN KEY(codFaixa) REFERENCES Faixa(codFaixa)
		ON update cascade ON delete cascade, --Questao 4, item C		
		CONSTRAINT FK_FaixaCompositorCompositor FOREIGN KEY(codCompositor) REFERENCES Compositor(codCompositor)
	) on BDSpotPerFG1

	Create Table FaixaPlaylist
	(
		codPlay int not null,
		codFaixa int not null,

		CONSTRAINT PK_FaixaPlaylist PRIMARY KEY(codPlay,codFaixa),
		CONSTRAINT FK_FaixaPlaylistPlaylist FOREIGN KEY(codPlay) REFERENCES Playlist(codPlay),
		CONSTRAINT FK_FaixaPlaylistFaixa FOREIGN KEY(codFaixa) REFERENCES Faixa(codFaixa)
		ON update cascade ON delete cascade --Questao 4, item C
	) on BDSpotPerFG2

	Create Trigger TR_PreçoCompra on Album
	for insert,update
	as
	if (Select preçoCompra 
		From inserted) > 3 * 
		(Select avg(a.preçoCompra) 
	 		From Album a
	 		Where codAlbum in
	    	(Select f1.codAlbum  
	    	From Faixa f1 
	    	Where f1.tipoGravação = 'DDD' 
	    	Group by codAlbum
	     	Having count(f1.codFaixa) = (Select count(f2.codFaixa) 
	     								From Faixa f2 
	     								Where f1.codAlbum = f2.codAlbum 
	     								Group By codAlbum)))
	
	Begin
	raiserror('Preço de compra invalido!', 25,1)
	Rollback transaction
	End
	
	
	-- Questao 3 --

	DROP INDEX PK_Album ON Faixa

	Create Clustered 
	Index IN_FaixaAlbum 
	ON Faixa(codAlbum) 
	With (pad_index = on, fillfactor = 100)

	Create NonClustered 
	Index IN_FaixaComposição 
	ON Faixa(codComposição) 
	With (pad_index = on, fillfactor = 100) 

	-- Questao 4 --
	-- Item A -- 

	Create Trigger TR_BarrocoDDD on FaixaCompositor
	for insert,update
	as
	if(Select tipoGravação
		From inserted i, faixa f
		Where i.codFaixa = f.codFaixa AND codCompositor in (Select C.codCompositor
															From Compositor C, PeriodoMusical pm 
															Where C.codPer = PM.codPer AND PM.codPer like '%Barroco%'))
															!= 'DDD'
	
	Begin
	raiserror('Condição BarrocoDDD não satisfeita', 34,1)
	Rollback transaction
	End

	-- Item B --

	Create Trigger TR_Faixa64 on Faixa
	for insert,update
	as
	if 16 < any(select count(f.codFaixa) 
				from faixa f
				group by codAlbum)

	begin
	raiserror('64 Faixas ultrapassadas', 23,1)
	rollback transaction
	end

	-- Questao 7 --

	Create View v1 (nome_Playlist, qtdAlbuns)
	as
	Select p.nome ,count(a.codAlbum)
	From Playlist p 
		inner join infoPlaylist ip ON p.codPlay = ip.codPlay
		inner join Faixa f ON ip.codFaixa = f.codFaixa
		inner join Album a ON f.codAlbum = a.codAlbum
	Group By p.nome
	-- Questao 8 --
	-- Item A (Gravadora com maior media de preço de compra?) --

	Select g.nome
	From Gravadora g
		inner join Album a1 ON g.codGrav = a1.codGrav
	Group By g.nome
	Having avg(a1.preçoCompra) >= all(Select avg(a2.preçoCompra)
									From Album a2
									Group By codGrav)	

	-- Item B --

	Select g.nome
	From Gravadora g
		inner join Album a ON g.codGrav = a.codGrav
		inner join Faixa f ON a.codAlbum = f.codAlbum
		inner join FaixaCompositor fc ON f.codFaixa = fc.codFaixa
		inner join Compositor c ON fc.codCompositor = c.codCompositor
		inner join FaixaPlaylist fp ON f.codFaixa = fp.codFaixa
	Where c.nome = 'Dvorack'
	Group by g.nome, c.nome
	Having count(fp.codPlay) >= all(Select count(fp1.codPlay)
									From Faixa f1
										inner join FaixaCompositor fc1 ON f1.codFaixa = fc1.codFaixa
										inner join Compositor c1 ON fc1.codCompositor = c1.codCompositor
										inner join FaixaPlaylist fp1 ON f1.codFaixa = fp1.codFaixa
									Where c.nome = 'Dvorack'
									Group By fp1.codPlay) 
	-- item C --

	Select Distinct(a.descrição) 
	From Faixa f
		inner join FaixaCompositor fc ON f.codFaixa = fc.codFaixa
		inner join Compositor c ON fc.codCompositor = c.codCompositor
		inner join Album a ON f.codAlbum = a.codAlbum
	where c.nome = 'Bach'

	-- item D --

	Select c.nome
	From Compositor c
		inner join FaixaCompositor fc ON c.codCompositor = fc.codCompositor
		inner join Faixa f ON fc.codFaixa = f.codFaixa
		inner join FaixaPlaylist fp ON f.codFaixa = fp.codFaixa
	Group By c.nome
	Having count(fp.codFaixa) >= all(Select count(fp.codFaixa)
									From Compositor c
										inner join FaixaCompositor fc ON c.codCompositor = fc.codCompositor
										inner join Faixa f ON fc.codFaixa = f.codFaixa
										inner join FaixaPlaylist fp ON f.codFaixa = fp.codFaixa
									Group By c.nome)
	-- item E --

	Select p.nome
	From Playlist p
		inner join FaixaPlaylist fp ON p.codPlay = fp.codPlay
		inner join Faixa f ON fp.codFaixa = f.codFaixa
		inner join Composição c1 ON f.codComposição = c1.codComposição
		inner join FaixaCompositor fc ON f.codFaixa = fc.codFaixa
		inner join Compositor c2 ON fc.codCompositor = c2.codCompositor
		inner join PeriodoMusical pm ON c2.codPer = pm.codPer
	Where pm.descrição = 'Barroco' AND c1.descrição = 'Concerto'
	Group By p.nome, p.codPlay
	Having count(f.codFaixa) = (Select count(f1.codFaixa)
								From faixa f1
									inner join FaixaPlaylist fp1 ON f1.codFaixa = fp1.codFaixa
									inner join Playlist p1 ON fp1.codPlay = p1.codPlay
								Where p.codPlay = p1.codPlay
								Group By p1.nome) 