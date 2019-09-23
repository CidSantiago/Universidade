function img (url) {
    str = '<img src="'+url+'" alt="Imagem da capa do livro" width = "100">'; 
    return str;
}

function lojas(data) {
    loja = data.lojas;
    let str = "";
    for (let index = 0; index < Object.keys(loja).length; index++) {

        str += '<h3 class="'+ loja[index].nome +'"> '+ loja[index].nome +'</h3>'; 
        str += '<div id="imagemloja">';
        str += '<img src="'+ loja[index].img +'" alt="Imagem da loja '+loja[index].nome +'" width="100">'
        str += '</div> <br>';

        if (loja[index].fisica != "") {
            str += '<a href="'+ loja[index].fisica +'">Versão Física</a><br>';
        }
        if (loja[index].digital != "") {
            str += '<a href="'+ loja[index].digital +'">Versão Digital</a><br>';
        }
        if (loja[index].capAval != "") {
            str += '<a href="'+ loja[index].capAval +'">Capítulo de Avaliação disponível.</a><br>';
        }
        if (loja[index].localizacao != "") {
            str += '<a href="'+ loja[index].localizacao +'">Localização</a><br>';
        }

        str += '<b>Avaliação: </b>'+loja[index].aval;

    }

    return str;
}

function livrosemelhantes(data) {
    semelhantes = data.livrosemelhantes;
    let str ="";

    for (let index = 0; index < Object.keys(semelhantes).length; index++) {
        
        str += '<h3>'+ semelhantes[index].nome + '</h3>';
        str += '<a href="'+ semelhantes[index].url +'" target="_self">';
        str += '<img src="'+ semelhantes[index].img +'" alt="Imagem do livro '+ semelhantes[index].nome+'" width="100">';
        str += '</a>';
    }

    return str;
}


function resenhas(data) {
    resenha = data.resenhas;
    let str = "";

    for (let index = 0; index < Object.keys(resenha).length; index++) {
        
        str += '<h4 class="user-resenha">'+ resenha[index].user +'</h4>';
        str += '<p class="texto-resenha">';
        str += resenha[index].texto;
        str += '</p>';
        str += '<p class="aval-resenha">';
        str += resenha[index].aval;
        str += '</p>';
    }
    
    return str;

}

function loadDoc(url) {
    fetch(url)
      .then(response => {
        response.json().then( (data) => {
            document.getElementsByClassName("titulo-livro")[0].innerHTML = data.nomelivro;
            document.getElementById("imagemlivro").innerHTML = img(data.imglivro);
            document.getElementsByClassName("autor-livro")[0].innerHTML = data.nomeautor;
            document.getElementById("imagemautor").innerHTML = img(data.imgautor);
            document.getElementsByClassName("descricao")[0].innerHTML = data.desclivro;
            document.getElementById("imguser").innerHTML = img(data.imgusuario);
            document.getElementById("nomeusuario").innerHTML = data.nomeusuario;
            document.getElementsByClassName("genero")[0].innerHTML = "<b>Genero: </b>"+data.genero;
            document.getElementsByClassName("numpaginas")[0].innerHTML = "<b>Numero de páginas: </b>"+data.numpaginas;
            document.getElementsByClassName("Editora")[0].innerHTML = "<b>Editora: </b>"+data.editora;
            document.getElementsByClassName("Idioma")[0].innerHTML = "<b>Idioma: </b>"+data.idioma;
            document.getElementsByClassName("ISBN-10")[0].innerHTML = "<b>ISBN-10: </b>"+data.ISBN10;
            document.getElementsByClassName("ISBN-13")[0].innerHTML = "<b>ISBN-13: </b>"+data.ISBN13;
            document.getElementsByClassName("peso")[0].innerHTML = "<b>Peso: </b>"+data.peso;
            document.getElementById("lojas").innerHTML = lojas(data);
            document.getElementById("semelhantes").innerHTML = livrosemelhantes(data);
            document.getElementsByClassName("numresenhas")[0].innerHTML = Object.keys(data.resenhas).length +" Resenhas";
            document.getElementsByClassName("avalsite")[0].innerHTML = data.avalmedia;
            document.getElementById("resenhas").innerHTML = resenhas(data);
        });
      }).catch(err => {
        console.error('Failed retrieving information', err);
      });
}

loadDoc("/data/livro2/data.json");
