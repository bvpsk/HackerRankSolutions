import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the sockMerchant function below.
    static int sockMerchant(int n, int[] ar) {
        int[] freq = new int[n];
        int[] check = new int[n];
        int c = 0, count;
        for(int i = 0;i < n;i++){
            freq[i] = -1;
        }
        for(int i = 0;i < n;i++){
            count = 1;
            for(int j = i+1;j < n;j++){
                if(ar[i] == ar[j]){
                    count += 1;
                    freq[j] = 0;
                }
            }
            if(freq[i] != 0){
                freq[i] = count;
                check[c] = i;
                c += 1;
            }
        }
        int sum = 0;
        for(int i = 0;i < c;i++){
            sum += freq[check[i]]/2;
        }
        return sum;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] ar = new int[n];

        String[] arItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arItem = Integer.parseInt(arItems[i]);
            ar[i] = arItem;
        }

        int result = sockMerchant(n, ar);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
