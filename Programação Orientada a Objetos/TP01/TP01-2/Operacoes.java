import java.util.Scanner;

public class Operacoes{
  public static void main (String[] args) { 
    Scanner scanner = new Scanner (System.in);
    
    float a,b,r;
    String op;
    System.out.println("Digite os numeros que ser�o utilizados ( A sequ�ncia importa )");
    a = scanner.nextFloat();
    b = scanner.nextFloat();
    System.out.println("Digite a opera��o desejada:");
    op = scanner.next();
    
    if ( op.equals("+")){
      r = a+b;
      System.out.println ("O resultado da adi��o de "+a+" com "+b+" � "+r+".");
    }
    else if ( op.equals("-")){
      r = a - b;
      System.out.println("O resultado da subtra��o de "+a+" com "+b+" � "+r+".");
    }
    else if( op.equals("*")){
      r = a * b;
      System.out.println("O resultado da multiplica��o de "+a+" com "+b+" � "+r+".");
    }
    else if ( op.equals("/")){
      r = a / b;
      System.out.println("O resultado da multiplica��o de "+a+" com "+b+" � "+r+".");
    }
  }
}
