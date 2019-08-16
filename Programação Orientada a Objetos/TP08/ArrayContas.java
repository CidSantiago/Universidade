
public class ArrayContas implements IRepositorioConta{

	private indice = 0;
	private ContaAbstrata[] contas;

	public ArrayContas{
		contas = new ContaAbstrata[100];    
	}

	public void inserir(ContaAbstrata conta){
		contas[indice] = conta;
        indice++;
	}

	public void remover(String numero){
		if( this.procurar(numero)!= null){
			
		}
	}
	ContaAbstrata procurar(String numero);
	ContaAbstrata[] listar();
	int tamanho();
}