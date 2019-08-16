public class CriaConta{
    
    public static void main (String args[]) {
        Conta conta;
        conta = new Conta ("13.013-4");
        conta.creditar(500.87);
        conta.debitar(45.00);
        System.out.println(conta.saldo());
    }
}
