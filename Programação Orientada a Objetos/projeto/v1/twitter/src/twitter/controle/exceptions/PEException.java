package twitter.controle.exceptions;

public class PEException extends MyTwitterException {

	private static final long serialVersionUID = 1L;

	public PEException(String usuario) {
			super("Perfil "+ usuario + " já existente!");
	}
}
