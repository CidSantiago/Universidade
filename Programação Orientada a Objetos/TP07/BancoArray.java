
public class BancoArray {
    
    private ContaAbstrata[] contas;
    private int indice=0;
    private double juros = 0.005;

    public BancoArray(){
            contas = new ContaAbstrata[100];     
    }
    
    
    public void cadastrar(ContaAbstrata conta){
        contas[indice] = conta;
        indice++;
    }
    
    private ContaAbstrata procurar(String numero){
        int i = 0;
        boolean achou = false;
        while ((!achou) && (i < indice)) {
            if (contas[i].numero().equals(numero)) {
                achou = true;
            } else {
                i++;
            }
        }
        if (achou == true) {
            return contas[i];
        } else {
            return null;
        }
    }
    
    public void creditar(String numero, double valor){
        ContaAbstrata conta;
        conta = procurar(numero);
        if (conta != null ){
            conta.creditar(valor);
        } else {
            System.out.println("Conta inexistente!");
        }
    }
    
    public void debitar(String numero, double valor){
        ContaAbstrata conta;
        conta = procurar(numero);
        if (conta != null ){
            conta.debitar(valor);
        } else {
            System.out.println("Conta inexistente!");
        }
    }
    
    public double saldo(String numero) {
        ContaAbstrata conta;

        conta = procurar(numero);
        if (conta!= null){
            return conta.saldo();
        } else {
            System.out.println("Conta inexistente!");
            return 0;
        }
        

    }
    
    public void transferir(String origem, String destino, double valor){
        ContaAbstrata contadestino;
        ContaAbstrata contaorigem;
        contadestino = procurar(destino);
        contaorigem = procurar(origem);
        
        if (contaorigem != null && contadestino != null && contaorigem.saldo() > valor){
            contaorigem.debitar(valor);
            contadestino.creditar(valor);
        } else if ( contaorigem == null){
            System.out.println("ContaAbstrata de origem inexistente!");
        } else if (contaorigem.saldo()<=valor) {
            System.out.println("Que pena, por motivos quantitativos voce nao pode realizar essa transacao :c");
        } else {
            System.out.println("Conta de destino inexistente!");
         }
        }

    public void renderJuros (String numero){
    	ContaAbstrata conta;
    	conta = procurar(numero);

    	if (conta != null && conta instanceof ContaPoupanca){
    		((ContaPoupanca)conta).renderJuros(juros);
    	} else{
    		System.out.println("Conta inexistente ou tipo errado");
    	}
    }
   
   public void renderBonus(String numero){
    ContaAbstrata conta;
    conta = procurar(numero);

    if (conta != null && conta instanceof ContaEspecial){
        ((ContaEspecial)conta).renderBonus();
    } else{
        System.out.println("Conta inexistente ou tipo errado");
    }
   }
   
}