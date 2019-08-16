public class CompactDisc extends Midia{
	
	public String album;
	public String artista;
	public int faixas;

	public CompactDisc(int cod){
		codigo = ("CD"+cod);
	}

	public void definirAlbum(String alb){
		album = alb;
	}

	public void definirArtista(String art){
		artista = art;
	}

	public void definirFaixas(int numero){
		faixas = numero;
	}

	public void imprimir (){
		System.out.ln("Album: "+album);
		System.out.ln("Artista: "+artista);
		System.out.ln("Quantidade de faixas: "+faixas);
		System.out.ln("Tempo de reprodução: "+tempo[0]+" minutos e "+tempo[1]+" segundos.");
		System.out.ln("Comentário: "+comentario);
		System.out.ln("Possui a mídia?: " + (if (gotIt==true){return "Sim";}else{return "Não";}))
	}
}