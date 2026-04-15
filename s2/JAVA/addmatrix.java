import java.util.Scanner;
public class addmatrix{

	public static void main(String args[]){
		int arr1[][] = new int[3][3];
		int arr2[][] = new int[3][3];
		int arr3[][] = new int[3][3];

		System.out.println("Enter matrix one: ");
		Scanner sc = new Scanner(System.in);
		
		for(int i =0; i<3; i++){
			for( int j=0; j<3; j++){
				arr1[i][j] = sc.nextInt();
			}
		}                                                     

		System.out.println("Enter matrix two: ");     	
                
	        for(int i =0; i<3; i++){
                	for( int j=0; j<3; j++){
                		arr2[i][j] = sc.nextInt();
                	}
                }      
	

		//add arrays
		 for(int i =0; i<3; i++){
                	for( int j=0; j<3; j++){
                		arr3[i][j] = arr1[i][j] + arr2[i][j]; 
                	}
                } 

 	        //diplay sum array
		System.out.println("The sum is");
                for(int i =0; i<3; i++){
                	for( int j=0; j<3; j++){
                		System.out.print(arr3[i][j] + "\t" );
			}
			System.out.println();
		}
	}
}   
		           
