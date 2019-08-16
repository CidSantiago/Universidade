package twitter.controle;

import twitter.controle.exceptions.*;
import twitter.perfils.Perfil;
import twitter.tweet.Tweet;
import java.util.Vector; 

public interface ITwitter {

		public void criarPerfil(Perfil usuario) throws PEException, MyTwitterException;
		
		public void cancelarPerfil(String usuario) throws PIException, PDException, MyTwitterException;
		
		public void tweetar(String usuario, String mensagem) throws PIException, MFPException, MyTwitterException;
		
		public Vector<Tweet> timeline(String Usuario) throws PIException, PDException;
		
		public Vector<Tweet> tweets (String Usuario) throws PIException, PDException;
		
		public void seguir(String seguidor, String seguido) throws PIException, PDException, SIException, MyTwitterException;
		
		public int numeroSeguidores (String usuario) throws PIException, PDException ;
		
		public Vector<Perfil> seguidores(String usuario) throws PIException, PDException;

}
