//Server using Server-side proccessing
const fs = require('fs-extra');
const express = require('express');
const expressLayouts = require('express-ejs-layouts'); 
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const path = require('path');
const multer = require('multer');

var app = express();

const hostname = '127.0.0.1';
const port = 8080;
const maxSize = 0.5*1024*1024; // 0.5MB

app.set('view engine','ejs');
app.use(express.static("public"));
app.use(cookieParser());
app.use(expressLayouts) 

app.get('/', (req, res) => {
	var dirData = path.join(__dirname+'/public/data/livros/');
	fs.readdir(dirData, function(err, items) {
	    livrosDisponiveis = items;
		
		// Carrega cookie
		var lastBook = req.cookies.lastBook;
		var short = [];

		// Visualizacao de conteudo do cookie
		if (lastBook != undefined) {
			var dirLastBook = path.join(dirData+'/'+lastBook+'/short.json');
			var data = JSON.parse(fs.readFileSync(dirLastBook));
			console.log('Cookie:'+ lastBook+'\n');
		} else {
			console.log('Cookie: Não Inicializado\n');
		}
		
		livrosDisponiveis.forEach(book => {
			var dirBook = path.join(dirData+'/'+book+'/short.json');
			var data = JSON.parse(fs.readFileSync(dirBook));
			short.push(data);
		});

		res.render('home', {short, data, lastBook});
	});
})	

app.get('/book/:usu', function (req, res) {
	var dirData = path.join(__dirname+'/public/data/livros/'+req.params.usu+'/data.json');
	var data = JSON.parse(fs.readFileSync(dirData));
	
	res.cookie('lastBook', req.params.usu);
    res.render('book', data);
});

app.get('/edit/:usu', function (req, res) {
	var dirData = path.join(__dirname+'/public/data/livros/'+req.params.usu+'/data.json');
	var data = JSON.parse(fs.readFileSync(dirData));
    res.render('editbook', data);
});

app.get('/config', function (req, res) {
    res.render('config');
});

app.get('/create', function (req, res) {
	res.render('createbook');
});

app.get('/delet/:bookid', function (req, res) {
	var dirData = path.join(__dirname+'/public/data/livros/'+req.params.bookid+'/short.json');
	var short = JSON.parse(fs.readFileSync(dirData)); 
	res.render('deletbook',short);
});


app.get('/delet/:bookid/confirmed', function (req, res) {
	var dirData = path.join(__dirname+'/public/data/livros/'+req.params.bookid);
	var dirBin = path.join(__dirname+'/public/bin/'+req.params.bookid)
	
	if (fs.existsSync(dirBin)) {
		fs.removeSync(dirBin);
	}

	fs.move(dirData,dirBin, function (err) {
		if (err) {
			return console.log(err);
		}
		console.log("Folders moved!");
	});
	
	if (req.cookies.lastBook == req.params.bookid) {
		res.clearCookie('lastBook');
	}

	res.send('<h2>Exclusão realizada com sucesso! </h2>'+
	'<a href="/">Voltar para home</a>')
});

app.post('/create/upload', function (req, res) {

	var upload = path.join(__dirname + '/public/uploads');

	var dataStorage = multer.diskStorage({
		// destino do arquivo
		destination: function (req, file, cb) {
			cb(null, upload)
		},
		// nome do arquivo
		filename: function (req, file, cb) {
			cb(null, file.fieldname+'.jpg');
		}
	});
	
	// utiliza a storage para configurar a instância do multer
	var dataUpload = multer({
		storage : dataStorage,
		limits  : { fileSize: maxSize }
	}).fields([
		{name: 'formimglivro'},
		{name: 'formimgautor'},
		{name: 'formimgloja'},
		{name: 'formimgusuario'}
	]);

	dataUpload(req, res, function (err) {
		if (err) {
			res.send(' <h2>O seu upload NÃO foi realizado! </h2> <br>'+
			'erro: '+ err.message +'<br>'+
			'<a href="/">Voltar para home</a>');
            return console.log(err);
		}
		
		var bookid = req.body.formidlivro;
		var direct = path.join(__dirname + '/public/data/livros/'+bookid);
		
		if (fs.existsSync(upload+'/formimglivro.jpg')) {
			fs.mkdir(direct);
			fs.renameSync(upload+'/formimglivro.jpg',direct+'/'+bookid+'.jpg');
		}

		var autor = req.body.formnomeautor.split(" ");
		var dirAutor = path.join(__dirname + '/public/data/autores');
		if (fs.existsSync(upload+'/formimgautor.jpg')) {
			fs.renameSync(upload+'/formimgautor.jpg',dirAutor+'/'+autor[0]+'.jpg');
		}
		
		var loja = req.body.formlojanome.split(" ");
		var dirLoja = path.join(__dirname + '/public/data/lojas');
		if (fs.existsSync(upload+'/formimgloja.jpg')) {
			fs.renameSync(upload+'/formimgloja.jpg',dirLoja+'/'+loja[0]+'.jpg');
		}

		var usuario = req.body.formusuarionome.split(" ");
		var dirUsuario = path.join(__dirname + '/public/data/usuarios');
		if (fs.existsSync(upload+'/formimgusuario.jpg')) {
			fs.renameSync(upload+'/formimgusuario.jpg',dirUsuario+'/'+usuario[0]+'.jpg');
		}
		
		var data = {
		"id":" ",
		"nomelivro":" ",
		"nomeautor": " ",
		"imglivro": " ",
		"imgautor": " ",
		"desclivro":" ",
		"nomeusuario": " ",
		"imgusuario": " ",
		"genero": " ",
		"numpaginas": " ",
		"editora": " ",
		"idioma": " ",
		"ISBN10": " ",
		"ISBN13": " ",
		"peso": " ",
		"lojas": " ",
		"livrosemelhantes": " ",
		"avalmedia":" ",
		"resenhas":" "
		};

		data.id = bookid;
		data.nomelivro = req.body.formnomelivro;
		data.nomeautor = req.body.formnomeautor;
		data.imglivro = "/data/livros/"+bookid+'/'+bookid+'.jpg';
		data.imgautor = "/data/autores/"+autor[0]+'.jpg';
		data.desclivro = req.body.formdescricao;
		data.genero = req.body.formgenero;
		data.numpaginas = req.body.formnumpaginas;
		data.editora = req.body.formeditora;
		data.idioma = req.body.formidioma;
		data.ISBN10 = req.body.formISBN10;
		data.ISBN13 = req.body.formISBN13;
		data.peso = req.body.formpeso;
		data.lojas = [ {
			"nome": req.body.formlojanome, 
            "img": "/data/lojas/"+loja[0]+'.jpg', 
            "fisica": req.body.formlojafisica, 
            "digital": req.body.formlojadigital,
            "capAval": req.body.formlojacapAval, 
			"localizacao": req.body.capAval, 
            "aval": ""
		}];
		data.nomeusuario = req.body.formusuarionome;
		data.imgusuario = "/data/usuarios/"+usuario[0]+'.jpg';
		data.resenhas = [];
		
		if (fs.existsSync(path.join(__dirname + '/public/data/livros/'+req.body.formsemelid))){
			var dir = path.join(__dirname + '/public/data/livros/'+req.body.formsemelid+'/short.json')
			var semelShort = JSON.parse(fs.readFileSync(dir));
			var short = {
				"nome": semelShort.nomelivro,
				"url": semelShort.id,
				"img":semelShort.imglivro
			}
			data.livrosemelhantes = [short];
		}


		short = { 
			"nomelivro": "",
			"imglivro": "",
			"avalmedia":"",
			"id":""
		}
		
		short.nomelivro = req.body.formnomelivro;
		short.imglivro = "/data/livros/"+bookid+'/'+bookid+'.jpg';
		short.id = req.body.formidlivro;

		fs.writeFile(direct + '/data.json', JSON.stringify(data), function (err, data){
			if (err) {
				console.log('Erro gravando o arquivo data.json');
				return console.error(err);
			}
		});

		fs.writeFile(direct + '/short.json', JSON.stringify(short), function (err, data){
			if (err) {
				console.log('Erro gravando o arquivo short.json');
				return console.error(err);
			}
		});

		res.send('<h2>Upload realizado com sucesso! </h2>'+
        '<a href="/">Voltar para home</a>');
	});
});


app.post('/edit/:bookid/upload', function (req, res) {
	
	var bookid = req.params.bookid;
	var direct = path.join(__dirname + '/public/data/livros/'+bookid);
	var upload = path.join(__dirname + '/public/uploads');

	var bookImgstorage = multer.diskStorage({
		// destino do arquivo
		destination: function (req, file, cb) {
			cb(null, upload)
		},
		// nome do arquivo
		filename: function (req, file, cb) {
			cb(null, bookid + '.jpg');
		}
	});
	
	// utiliza a storage para configurar a instância do multer
	var bookImgupload = multer({
		storage : bookImgstorage,
		limits  : { fileSize: maxSize }
	}).single('formimglivro');

	bookImgupload(req, res, function (err) {
		if (err) {
			res.send(' <h2>O seu upload NÃO foi realizado! </h2> <br>'+
			'erro: '+ err.message +'<br>'+
			'<a href="/">Voltar para home</a>');
            return console.log(err);
		}
		

		if (fs.existsSync(upload+'/'+bookid+'.jpg')) {
			fs.renameSync(upload+'/'+bookid+'.jpg',direct+'/'+bookid+'.jpg');
		}

		var oldData = JSON.parse(fs.readFileSync(direct+'/data.json').toString());
		var oldShort = JSON.parse(fs.readFileSync(direct+'/short.json').toString());

		// Faltar atualizar loja no JSON
		oldData.nomelivro = req.body.formnomelivro;
		oldData.nomeautor = req.body.formnomeautor;
		oldData.desclivro = req.body.formdescricao;
		oldData.genero = req.body.formgenero;
		oldData.numpaginas = req.body.formnumpaginas;
		oldData.editora = req.body.formeditora;
		oldData.idioma = req.body.formidioma;
		oldData.ISBN10 = req.body.formISBN10;
		oldData.ISBN13 = req.body.formISBN13;
		oldData.peso = req.body.formpeso;
		
		oldShort.nomelivro = req.body.formnomelivro;

		fs.writeFile(direct + '/data.json', JSON.stringify(oldData), function (err, data){
			if (err) {
				console.log('Erro gravando o arquivo data.json');
				return console.error(err);
			}
		});

		fs.writeFile(direct + '/short.json', JSON.stringify(oldShort), function (err, data){
			if (err) {
				console.log('Erro gravando o arquivo short.json');
				return console.error(err);
			}
		});

		res.send('<h2>Upload realizado com sucesso! </h2>'+
        '<a href="/">Voltar para home</a>');
	});
});

app.listen( port, hostname, function () {
    console.log('Servidor rodando em http://'+hostname+':'+port+'/');
});