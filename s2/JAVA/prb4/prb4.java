import java.util.Scanner;
class negexception extends Exception{

	negexception(String s){
		super(s);
	}
}

public class prb4{

	public static void main(String args[]){

		//get file numbers
		
		System.out.println("Enter 5 numbers");
		Scanner sc = new Scanner(System.in);
		int sum = 0;
		
		
		for(int i =0; i<5; i++){

			while(true){
		
				try{

					int j = sc.nextInt();
					if(j < 0){
						throw new negexception("Negative number");
					}else{
						sum += j;
						break;
					}
				}catch(negexception e){

					System.out.println("Exception: " + e.getMessage());
				}
			}
		}
		
		System.out.println("sum: " + sum);

		System.out.println("avg: " + ((float)sum/5));
	}
}	
				


