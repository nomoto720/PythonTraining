import java.util.*;
public class Warikan{
	public static void main(String args[]){
		Scanner scan=new Scanner(System.in);
		System.out.print("料金を入力>>");
		int price=scan.nextInt();
		System.out.print("人数を入力>>");
		int number=scan.nextInt();
		int payment=price/number;
		System.out.printf("お支払いは%d円です%n",payment);
	}
}
