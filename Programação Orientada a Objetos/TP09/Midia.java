public abstract class Midia{

	public int tempo[2];
	public String comentario;
	public boolean gotIt;

	public Midia(int cod){
		this.codigo = cod;
		this.tempo[0]=-1;
		this.tempo[1]=-1;
	}

	public void definirTipo(int valor){
		this.tipo = valor;
	}

	public void definirTempo(int valor[2]){
		this.tempo[0] = valor[0];
		this.tempo[1] = valor[1];
	}

	public void definirComentario(String coment){
		this.comentario = coment;
	}

	public boolean definirGotIt(boolean tenho){
		this.gotIt = tenho;
	}

	public abstract void imprimir();
}