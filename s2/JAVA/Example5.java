class Example5{
	public static void main(String args[])
		{
		int x,y;
		y=20;
		for(x=0;x<10;x=x+1)
			{
				System.out.println("This is x:"+x);
				System.out.println("This is y:"+y);
				y=y-2;
				if(x==9)
					{
						continue;
					}
				System.out.println("\n next iteration\n");
			
			}
			System.out.println("\n iteration ended\n");
		}
	}
		
