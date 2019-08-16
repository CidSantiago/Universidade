import java.util.Scanner;

public class MaiorNumero {
  public static void main ( String[] args ){
    Scanner input = new Scanner (System.in);
    int a,b;
    System.out.println("Coloque os números desejados:");
    a = input.nextInt();
    b = input.nextInt();
    
    if (a>b){
      System.out.printf("O primeiro numero, que é %d , é maior que o segundo número, %d.\n", a,b);
    }
    else if (a<b){
      System.out.printf("O segundo número, que é %d, é maior que o primeiro número, %d\n.", a,b);
    }
    else{
      System.out.printf("Os dois números são iguais! %d = %d.\n", a,b);
      }
    }
  }
   