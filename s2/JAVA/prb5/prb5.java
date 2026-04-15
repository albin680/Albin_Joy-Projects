import java.util.Scanner;
class Tone extends Thread{
	public void run(){
		//multiplication table of 5
		int limit = 10;			
		for(int i=0; i<limit; i++){
			System.out.println("THREAD ONE: "+"5"+" x "+ i + " = " + (5*i));	
			Scanner sc = new Scanner(System.in);
			
			if(i == 45){
					
				
			}

		}
	}
}

class Ttwo extends Thread{
	public void run(){
		//n prime numbers
		int limit = 10;
			
		System.out.println("THREAD TWO: 2");
		for(int i = 3; i<limit; i++){
	
			int flag = 1;
			
			for(int j = 2; j<= i/2; j++){

				if(i%j == 0){
					flag=0;
					break;
				}
			}

			if(flag == 1){

				 	
				System.out.println("THREAD TWO: " +i);
			}

		}	

	}
}


public class prb5{

	public static void main(String[] args){
		
		Tone obj1 = new Tone();
		Ttwo obj2 = new Ttwo();
		
		obj1.start();
		obj2.start();
	}
}
