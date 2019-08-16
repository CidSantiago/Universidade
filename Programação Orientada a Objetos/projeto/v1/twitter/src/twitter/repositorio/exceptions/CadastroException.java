package twitter.repositorio.exceptions;

public class CadastroException extends RepositorioException {

	private static final long serialVersionUID = 1L;

	public CadastroException(String message, String usuario) {
			super(message, usuario);
	}
}
