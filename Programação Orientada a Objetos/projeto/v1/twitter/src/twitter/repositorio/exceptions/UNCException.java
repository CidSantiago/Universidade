package twitter.repositorio.exceptions;

public class UNCException extends RepositorioException {
	
	private static final long serialVersionUID = 1L;

	public UNCException(String message, String usuario) {
			super(message, usuario);
	}
}
