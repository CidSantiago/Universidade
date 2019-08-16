package twitter.controle;

import java.io.IOException;
import java.util.Vector;
import twitter.repositorio.IRepositorioUsuario;
import twitter.repositorio.exceptions.*;
import twitter.perfils.Perfil;
import twitter.tweet.Tweet;
import twitter.controle.exceptions.*;

public class MyTwitter implements ITwitter {

	private IRepositorioUsuario repositorio;
	
	public MyTwitter (IRepositorioUsuario repositorio){
	
		this.repositorio = repositorio;
	}
	
	@Override
	public void criarPerfil(Perfil usuario) throws PEException, MyTwitterException{
		try{
			repositorio.cadastrar(usuario);
		} 
		catch (UJCException ujc) {
			throw new PEException(usuario.getUsuario());
		}
		catch(CadastroException ce) {
			throw new MyTwitterException(ce);
		}
	}

	@Override
	public void cancelarPerfil(String usuario) throws PIException, PEException, MyTwitterException {
		Perfil perfil;
		if( repositorio.buscar(usuario) != null){
			perfil = repositorio.buscar(usuario);
			
			if (perfil.isAtivo()!= false){
				perfil.setAtivo(false);
			}
			else{
				throw new PDException(usuario);
			}
		}
		else{
			throw new PIException(usuario);
		}
		try {
			repositorio.atualizar(perfil);
		}
		catch(UNCException unc){
			throw new MyTwitterException(unc);
		}
		catch(IOException ioe){
			throw new MyTwitterException(ioe);
		}
	}

	@Override
	public void tweetar(String usuario, String mensagem) throws PIException, MFPException, MyTwitterException{
		Tweet tweet;
		Perfil perfil,seguidor;
		if(repositorio.buscar(usuario)!= null){
			if(mensagem.length()>0 && mensagem.length()<141){
				tweet = new Tweet(usuario,mensagem);
				perfil = repositorio.buscar(usuario);
				perfil.addTweet(tweet);
				for (int i = 0; i < numeroSeguidores(usuario); i++){
					if( repositorio.buscar(perfil.getSeguidores().get(i)) != null){
						seguidor = repositorio.buscar(perfil.getSeguidores().get(i));
						seguidor.addTweet(tweet);
						try{
							repositorio.atualizar(seguidor);
						}
						catch(UNCException unc){
							throw new MyTwitterException(unc);
						}
						catch(IOException ioe){
							throw new MyTwitterException(ioe);
						}
					}
					else{
						throw new MyTwitterException("Seguidor não existente!");
					}
				}
				try{
					repositorio.atualizar(perfil);
				}
				catch(UNCException unc){
					throw new MyTwitterException(unc);
				}
				catch(IOException ioe){
					throw new MyTwitterException(ioe);
				}
			}
			else{
				throw new MFPException(mensagem.length());
			}
		}
		else{
			throw new PIException(usuario);
		}
	}
	
	@Override
	public Vector<Tweet> timeline(String usuario) throws PIException, PDException {
		Vector<Tweet> timeline;
		Perfil perfil;
		
		if( repositorio.buscar(usuario)!= null){
			perfil = repositorio.buscar(usuario);
			
			if(perfil.isAtivo() == true){
				timeline = perfil.getTimeline();
				return timeline;
			}
			else{
				throw new PDException(usuario);
			}
		}
		else{
			throw new PIException(usuario);
		}
	}
	
	@Override
	public Vector<Tweet> tweets(String usuario) throws PIException, PDException {
		Vector<Tweet> tweets;
		Perfil perfil;
		int numtweets;
		tweets = new Vector<Tweet>();
		
		if (repositorio.buscar(usuario) != null){
			perfil = repositorio.buscar(usuario);
			if (perfil.isAtivo() == false){
				throw new PDException(usuario);
			}
		}
		else{
			throw new PIException(usuario);
		}
		
		numtweets = perfil.getTimeline().size();
		for (int i = 0; i < numtweets; i++){
			if(perfil.getTimeline().get(i).getUsuario() == usuario){
				tweets.add(perfil.getTimeline().get(i));
			}
		}
		return tweets;
	}

	@Override
	public void seguir(String seguidor, String seguido) throws PIException, PDException, SIException, MyTwitterException  {
		Perfil followed, follower;
		if (seguidor == seguido){
			throw new SIException(seguidor);
		}
		if (repositorio.buscar(seguido)!= null && repositorio.buscar(seguidor) != null){
			followed = repositorio.buscar(seguido);
			follower = repositorio.buscar(seguidor);
			if(followed.isAtivo() == true && follower.isAtivo() == true){
				followed.addSeguidor(seguidor);
				/*for (int i = 0; i < tweets(seguido).size(); i++){
					follower.addTweet(tweets(seguido).get(i));
				}*/
				try{
					repositorio.atualizar(followed);
					repositorio.atualizar(follower);
				}
				catch(UNCException unc){
					throw new MyTwitterException(unc);
				}
				catch(IOException ioe){
					throw new MyTwitterException(ioe);
				}
			}
			else if (followed.isAtivo() == false){
				throw new PDException(seguido);
			}
			else{
				throw new PDException(seguidor);
			}
		}
		else if (repositorio.buscar(seguido) == null){
			throw new PIException(seguido);
		}
		else{
			throw new PIException(seguidor);
		}
	}

	@Override
	public int numeroSeguidores(String usuario) throws PIException, PDException {
		Perfil perfil;
		int numseguidores;
		if(repositorio.buscar(usuario)!= null){
			perfil = repositorio.buscar(usuario);
			if(perfil.isAtivo()== true){
				numseguidores = perfil.getSeguidores().size();
				return numseguidores;
			}
			else{
				throw new PDException(usuario);
			}
		}
		else{
			throw new PIException(usuario);
		}
	}

	@Override
	public Vector<Perfil> seguidores(String usuario) throws PIException, PDException {
		Perfil perfil;
		Vector<Perfil> seguidores;
		int numseguidores;
		seguidores = new Vector<Perfil>();
		
		try{
			numseguidores = numeroSeguidores(usuario);
		}
		catch(PDException pde){
			throw new PDException(usuario);
		}
		catch(PIException pie){
			throw new PIException(usuario);
		}
		
		perfil = repositorio.buscar(usuario);
		for (int i = 0; i < numseguidores; i++){
			Perfil seguidor;
			seguidor = repositorio.buscar(perfil.getSeguidores().get(i));
			if(seguidor.isAtivo() == true )
			seguidores.add(repositorio.buscar(perfil.getSeguidores().get(i)));
		}
		return seguidores;
	}

}
