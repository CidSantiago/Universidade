package twitter.perfils;

import java.util.Vector;
import twitter.tweet.Tweet;

public abstract class Perfil {

	private String usuario;
	private Vector<String> seguidores;
	private Vector<Tweet> timeline;
	private boolean ativo;
	
	public Perfil(String usuario){
		this.usuario = usuario;
		seguidores = new Vector<String>();
		timeline = new Vector<Tweet>();
	}
	
	public void addSeguidor(String usuario) {
		seguidores.add(usuario);
	}
	
	public void addTweet(Tweet tweet){
		timeline.add(tweet);
	}
	
	public void setUsuario(String usuario){
		this.usuario = usuario;
	}
	
	public String getUsuario(){
		return usuario;
	}
	
	public Vector<String> getSeguidores(){
		return seguidores;
	}
	
	public Vector<Tweet> getTimeline(){
		return timeline;
	}
	
	public void setAtivo (boolean valor){
		ativo = valor;
	}
	
	public boolean isAtivo(){
		return ativo;
	}
	
}
