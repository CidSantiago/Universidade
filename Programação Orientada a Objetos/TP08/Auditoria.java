
public class Auditoria {
	
	public static void main(String args[]){
		BancoArray bancoArray = new BancoArray();
		BancoVector bancoVector = new BancoVector();
		AuditorBancoGenerico auditor = new AuditorBancoGenerico();
		auditor.auditar(bancoArray);
		auditor.auditar(bancoVector);
	}
}