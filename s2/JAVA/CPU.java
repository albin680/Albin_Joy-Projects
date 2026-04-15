public class CPU{

	double price;

	public class processor{

		int cores;
		String manufacturer;
		
		void info(int c, String m){
			cores = c;
			manufacturer = m;
		System.out.println("processor details");
		System.out.println("The manufacture is : " + m);
		System.out.println("The no. of cores is : " + c);
		}

	}

	static class ram{
		
		double memory;
		String manufacturer;

		void info( int mem, String m){
			memory = mem;
			manufacturer = m;

		System.out.println("ram details");
		System.out.println("The manufacture is : " + m);
		System.out.println("The amount of mem is : " + mem + "GB");
 
		}

	}



public static void main( String args[]){

	CPU Cpu = new CPU();
	CPU.processor Processor = Cpu.new processor();
	CPU.ram Ram = new CPU.ram();
	Processor.info(8,"Snapdragon");
	Ram.info(16,"APMH");
}


}
