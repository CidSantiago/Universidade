package twitter.tweet;

public class Tweet {
	
	private String usuario;
	private String mensagem;
	
	public Tweet(String usuario, String mensagem) {
		this.mensagem = mensagem;
		this.usuario = usuario;
	}
	
	public void setUsuario(String usuario){
		this.usuario = usuario;
	}
	
	public String getUsuario(){
		return usuario;
	}
	
	public void setMensagem(String mensagem){
		this.mensagem = mensagem;
	}
	
	public String getMensagem(){
		return mensagem;
	}
	
}
