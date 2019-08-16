package twitter.controle.exceptions;

public class MFPException extends MyTwitterException {

	private static final long serialVersionUID = 1L;

	public MFPException(int tamanho) {
			super("A mensagem possui "+tamanho+", que ultrapassa o limite de 140 caracteres");
	}
}
