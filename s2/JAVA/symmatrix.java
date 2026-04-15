import java.util.Scanner;
public class symmatrix{

	public static void main(String args[]){
		int arr1[][] = new int[3][3];
		int arr2[][] = new int[3][3];

		System.out.println("Enter matrix : ");
		Scanner sc = new Scanner(System.in);
		
		for(int i =0; i<3; i++){
			for( int j=0; j<3; j++){
				arr1[i][j] = sc.nextInt();
			}
		}                                                     

		 for(int i =0; i<3; i++){
                	for( int j=0; j<3; j++){
                		arr2[j][i] = arr1[i][j]; 
                	}
                }

		for(int i = 0 ;i<3;i++){
			for(int j = 0;j<3; j++){
				if (arr1[i][j] != arr2[i][j]){
					System.out.println("Not symmetric matrix");
					System.exit(0);
				}
			}
		}

		System.out.println("This is a symmetric matrix");
	}
}   
		                    
