//Server using Server-side proccessing
const fs = require('fs');
const express = require('express');
const expressLayouts = require('express-ejs-layouts'); 
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const path = require('path');

var app = express();

const hostname = '127.0.0.1';
const port = 8080;

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

app.get('/config', function (req, res) {
    res.render('config');
});

app.listen( port, hostname, function () {
    console.log('Servidor rodando em http://'+hostname+':'+port+'/');
});