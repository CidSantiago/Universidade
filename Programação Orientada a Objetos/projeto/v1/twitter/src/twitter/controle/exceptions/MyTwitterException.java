package twitter.controle.exceptions;

public class MyTwitterException extends Exception {
	
	private static final long serialVersionUID = 1L;

	private Exception cause;

	private String message;

	public MyTwitterException(String message) {
		this.message = message;
	}

	public MyTwitterException(Exception cause) {
		super("A��o n�o realizada!");
		this.cause = cause;
	}

	public String getMessage() {
		String text = "A��o n�o realizada!\nCausa: ";
		if (cause != null) {
			text += cause.getMessage();
		} else {
			text += message;
		}
		return text;
	}

	public Exception getCause() {
		return cause;
	}

}
