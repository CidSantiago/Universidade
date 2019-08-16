package twitter.repositorio.exceptions;

public class RepositorioException extends Exception {
	
	private static final long serialVersionUID = 1L;

	protected String usuario;

	protected String message;

	public RepositorioException(String message) {
		super("Repositorio Exception!");
		this.message = message;
	}

	public RepositorioException(String message, String usuario) {
		super("Repositorio Exception!");
		this.usuario = usuario;
		this.message = message;
	}

	public String getMessage() {
		return this.message + " [Usuario = " + usuario + "]";
	}

	public String getUsuario() {
		return usuario;
	}
}
