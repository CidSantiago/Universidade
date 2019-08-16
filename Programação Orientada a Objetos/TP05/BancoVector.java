import java.util.Vector;

public class BancoVector {
    
    private Vector<Conta> contas = new Vector<Conta>();
    private int indice =0;
    private double juros = 0.005;
    /* public Banco() {
            contas = new Conta[100];     
    }*/
    
    
    public void cadastrar(Conta conta){
        contas.add(indice,conta);
        indice++;
    }
    
    private Conta procurar(String numero){
        int i = 0;
        boolean achou = false;
        while ((!achou) && (i < indice)) {
            if (contas.get(i).numero().equals(numero)) {
                achou = true;
            } else {
                i++;
            }
        }
        if (achou == true) {
            return contas.get(i);
        } else {
            return null;
        }
    }
    
    public void creditar(String numero, double valor){
        Conta conta;
        conta = procurar(numero);
        if (conta != null ){
            conta.creditar(valor);
        } else {
            System.out.println("Conta inexistente!");
        }
    }
    
    public void debitar(String numero, double valor){
        Conta conta;
        conta = procurar(numero);
        if (conta != null ){
            conta.debitar(valor);
        } else {
            System.out.println("Conta inexistente!");
        }
    }
    
    public double saldo(String numero) {
        Conta conta;

        conta = procurar(numero);
        if (conta!= null){
            return conta.saldo();
        } else {
            System.out.println("Conta inexistente!");
            return 0;
        }
        

    }
    
    public void transferir(String origem, String destino, double valor){
        Conta contadestino;
        Conta contaorigem;
        contadestino = procurar(destino);
        contaorigem = procurar(origem);
        
        if (contaorigem != null && contadestino != null && contaorigem.saldo() > valor){
            contaorigem.debitar(valor);
            contadestino.creditar(valor);
        } else if ( contaorigem == null){
            System.out.println("Conta de origem inexistente!");
        } else if (contaorigem.saldo()<=valor) {
            System.out.println("Que pena, por motivos quantitativos voce nao pode realizar essa transacao :c");
        }else {
            System.out.println("Conta de destino inexistente!");
         }
    }

    public void renderJuros (String numero){
        Conta conta;
        conta = procurar(numero);

        if (conta != null && conta instanceof ContaPoupanca){
            ((ContaPoupanca)conta).renderJuros(juros);
        }
        else{
            System.out.println("Conta inexistente ou tipo errado");
        }
    }
}