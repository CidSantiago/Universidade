
public interface IRepositorioConta {
	
	void inserir(ContaAbstrata conta);
	void remover(String numero);
	ContaAbstrata procurar(String numero);
	ContaAbstrata[] listar();
	int tamanho();
}