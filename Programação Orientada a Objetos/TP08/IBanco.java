
public interface IBanco {

	double saldoTotal();
	int numeroContas();
	void cadastrar(ContaAbstrata conta);
	void creditar(String numero, double valor);
	void debitar(String numero, double valor);
	double saldo(String numero);
	void transferir(String origem, String destino, double valor);
	//Nao posso colocar private procurar. E agora?
}