import java.util.Scanner;

public class MaiorNumero {
  public static void main ( String[] args ){
    Scanner input = new Scanner (System.in);
    int a,b;
    System.out.println("Coloque os n�meros desejados:");
    a = input.nextInt();
    b = input.nextInt();
    
    if (a>b){
      System.out.printf("O primeiro numero, que � %d , � maior que o segundo n�mero, %d.\n", a,b);
    }
    else if (a<b){
      System.out.printf("O segundo n�mero, que � %d, � maior que o primeiro n�mero, %d\n.", a,b);
    }
    else{
      System.out.printf("Os dois n�meros s�o iguais! %d = %d.\n", a,b);
      }
    }
  }
   