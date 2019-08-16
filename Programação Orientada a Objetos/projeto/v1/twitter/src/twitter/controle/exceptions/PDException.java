package twitter.controle.exceptions;

public class PDException extends MyTwitterException {
	
	private static final long serialVersionUID = 1L;

	public PDException(String usuario) {
			super("Perfil "+ usuario + " já desativado!");
	}
}
