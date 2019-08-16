package twitter.repositorio.exceptions;

public class UJCException extends RepositorioException {

	private static final long serialVersionUID = 1L;

	public UJCException(String message, String usuario) {
			super(message, usuario);
	}
}
