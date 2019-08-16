package twitter.repositorio;

import java.io.IOException;

import twitter.perfils.Perfil;
import twitter.repositorio.exceptions.*;

public interface IRepositorioUsuario {
	
	public void cadastrar(Perfil usuario) throws UJCException, CadastroException;
	
	public Perfil buscar (String usuario);
	
	public void atualizar (Perfil usuario) throws UNCException, IOException;
	
}
