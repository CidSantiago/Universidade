
public class ContaImposto extends ContaAbstrata {

	public ContaImposto (String numero){
		super(numero);
	}

	public void debitar(double valor){
		saldo = saldo - (valor + (valor * 0.001));
	}
}