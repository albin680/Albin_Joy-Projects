//Arithmetic package with interface for the 4 basic arithmetic operations test the package with two given numbers
package Arithmetic;

interface Temp{
	
	void add();
	void sub();
	void div();
	void mul();
}

public class Algebra implements Temp{

	float num1;
	float num2;
	
	public Algebra(float a, float b){
		
		this.num1 = a;
		this.num2 = b;
	}

	public void add(){
		
		System.out.println("The SUM is: " + (this.num1+this.num2));
	}

	public void sub(){
		
		System.out.println("The DIFF is: " + (this.num1-this.num2));
	}

	public void mul(){

		System.out.println("The PROD is: " + (this.num1*this.num2));
	}

	public void div(){

		System.out.println("The QUOT is: " + (this.num1/this.num2));
	}
}
