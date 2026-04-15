import Arithmetic.Algebra;
import java.util.Scanner;

public class Prob2{

	public static void main(String[] args){

		Scanner sc = new Scanner(System.in);
		
		System.out.println("Enter your num1: ");
		int num1 = sc.nextFloat();

		System.out.println("Enter your num2: ");
		int num2 = sc.nextFloat();

		Algebra obj = new Algebra(num1, num2);

		obj.add();
		obj.mul();
		obj.div();
		obj.sub();
	}
}
