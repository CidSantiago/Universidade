import java.util.Scanner;

public class SegundoGrau{
    public static void main (String[] args){
        Scanner input = new Scanner (System.in);
        
        float a,b,c, eq;
        System.out.println("Digite os coeficientes a,b e c da equação de segundo grau (ax² + bx + c):");
        a = input.nextFloat();
        b = input.nextFloat();
        c = input.nextFloat();
        System.out.println("A equação é "+a+".x² + "+b+".x + "+c+" .");
        

        
    }
}
