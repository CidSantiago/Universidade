package twitter.controle.exceptions;

public class PIException extends MyTwitterException {

	private static final long serialVersionUID = 1L;

	public PIException(String usuario) {
			super("Perfil "+ usuario + " inexistente!");
	}
}
