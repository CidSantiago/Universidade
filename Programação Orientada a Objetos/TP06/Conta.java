public class Conta{
    private String numero;
    private double saldo;
    
    public Conta (String numero){
        this.numero = numero;
        saldo = 0;
    }
    
    public void creditar (double valor){
        saldo = saldo + valor;
    }
    
    public void debitar (double valor){
        saldo = saldo - valor;
    }
    
    public String numero () {
        return numero;
    }
    
    public double saldo (){
        return saldo;
    }
    
}
