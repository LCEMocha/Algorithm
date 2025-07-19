import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        long[] distance = new long[n-1];
        long[] price = new long[n];
        
        for (int i = 0; i < n-1; i++) {
            distance[i] = sc.nextLong();
        }
        
        for (int i = 0; i < n; i++) {
            price[i] = sc.nextLong();
        }
        
        long totalcost = 0;
        long minPrice = price[0];
        
        for (int i=0; i<n-1; i++) {
            if (price[i] < minPrice) {
                minPrice = price[i];
            }
            totalcost += minPrice * distance[i];
        }
        
        System.out.println(totalcost);
    }
    
    
}