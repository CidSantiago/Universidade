package twitter.controle.exceptions;

public class SIException extends MyTwitterException {

	private static final long serialVersionUID = 1L;

	public SIException(String usuario) {
			super("Seguidor Invalido! Um usuario nao pode se seguir! Usuario:@"+ usuario);
	}
}
