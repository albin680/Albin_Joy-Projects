import java.util.Scanner;

class credexception extends Exception{
	public credexception(String s){
		super(s);
}
}

public class Mainclass{


	public static void main( String args[]){


		Scanner sc = new Scanner(System.in);

		System.out.println("Enter the username: ");
		String name = sc.next();
		System.out.println("Enter the password: ");
		String password = sc.next();

		try{

			if( name.equals("albin") && password.equals("mone")){
				System.out.println("Access granted");
			}else{
				throw new credexception( "Invalid Credentials" );
			}

		}catch(credexception e){

			System.out.println(e.getMessage());
		}

	}
}
