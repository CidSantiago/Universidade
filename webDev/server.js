//Server using Server-side proccessing
const fs = require('fs');
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

// Verificar utilização do :usu
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