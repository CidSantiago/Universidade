
public class ContaPoupanca extends Conta {
	
	public ContaPoupanca (String numero){
		super(numero);

	}

	public void renderJuros(double taxa){
		 super.creditar(super.saldo()*taxa);

	}

}