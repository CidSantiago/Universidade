//Server using Server-side proccessing
const fs = require('fs');
const express = require('express');
var app = express();

const hostname = '127.0.0.1';
const port = 8080;

const data1 = JSON.parse(fs.readFileSync("./data/livro1/data.json"));
const data2 = JSON.parse(fs.readFileSync("./data/livro2/data.json"));
const data3 = JSON.parse(fs.readFileSync("./data/livro3/data.json"))

app.set('view engine','ejs');
app.use(express.static("public"));

app.get('/', function (req, res) {
    res.render('home', data1);
});

app.get('/shining.html', function (req, res) {
    res.render('home', data2);
});

app.get('/home.html', function (req, res) {
    res.render('home', data1);
});

app.get('/carie.html', function (req, res) {
    res.render('home', data3);
});


app.listen( port, hostname, function () {
    console.log('Servidor rodando em http://'+hostname+':'+port+'/');
});

// Server using client-side proccessing
/*
var http = require('http');
var url = require('url');
var fs = require('fs');

http.createServer(function (req, res) {
	var q = url.parse(req.url,true); 
	var filename = "."+q.pathname;
	fs.readFile(filename, function(err,data) {
		if (err) {
			res.writeHead(404, {'Content-Type':'text/html'});
			return res.end("404 File Not Found");
		}
		res.writeHead(200);
		res.write(data);
		return res.end();
	});
}).listen(8080); 
console.log("Aguardando requisicoes na porta 8080!");
*/