import java.util.Scanner;

class employee {
	
		
		int eNo, eSalary;
		
		String eName;
		
		public void edata() {
		
		Scanner in = new Scanner(System.in);
		
		System.out.println("enter the employ number : ");
		
		eNo = in.nextInt();
		
		System.out.println("enter the employ name : ");
		
		eName = in.next();
		
		System.out.println("enter the employ salary  : ");
		
		eSalary = in.nextInt();
		
	
	}
		void data() {
			
		
			System.out.println("id number : "+eNo);
			
			System.out.println(" name : "+eName);
			
			System.out.println(" salary : "+eSalary);
		}
		
}

public class one{

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		
		System.out.println("enter the number of employees : ");
		
		int n = in.nextInt();
		
		employee a[] = new employee[n];
		
		
		System.out.println("-enter the employee details-");
		
		for(int i = 0; i < n; i ++) {
			
			a[i] = new employee();
			
			a[i].edata();
			
			
		}
		
		System.out.println("----------INFORMATION-----------");
		System.out.println("enter the id of the employee : ");
		
		int k = in.nextInt();
		
		
		for(int  i = 0 ; i < n ; i ++) {
			
			if (k == a[i].eNo){
				
				a[i].data();
			
			}
		}
		
		
		
	}

}

