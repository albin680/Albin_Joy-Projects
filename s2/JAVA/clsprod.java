class prod{
	String pcode;
	String pname;
	int price;
	}
	class clsprod {
		public static void main (String args[]){
		prod prod1 = new prod ();
		prod prod2 = new prod ();
		prod prod3 = new prod ();
		
			prod1.pcode = "ABC123";
			prod1.pname = "Mouse";
			prod1.price = 4566;
			
			prod2.pcode = "DEF123";
			prod2.pname = "Monitor";
			prod2.price = 45621;
			
			prod3.pcode = "GHI123";
			prod3.pname = "KeyBoard";
			prod3.price = 456;
			
			if (prod1.price > prod2.price && prod1.price > prod3.price)
				System.out.println("Highest price is " + prod1.price);
					else if (prod2.price > prod1.price && prod2.price > prod3.price)
						System.out.println("Highest price is " + prod2.price);
							else if(prod3.price > prod1.price && prod3.price > prod2.price)
								System.out.println("Highest price is " + prod3.price);
									else
										System.out.println("All price are same");
			}
			}
	
	
