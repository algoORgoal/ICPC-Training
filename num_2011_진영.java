import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
   public static void main(String[] args) throws NumberFormatException, IOException {
      // TODO Auto-generated method stub
      BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

      String input = bf.readLine();
      
      if(input.charAt(0) == '0') {
         System.out.println(0);
         bf.close();
         return;
      }
      
      final int MOD = 1000000;
      int[] dp = new int[input.length() + 1];
      dp[0] = dp[1] = 1;
      
      for(int i = 2; i <= input.length(); i++) {
         int first = i - 1;
         
         if(input.charAt(first) > '0') {
            dp[i] = dp[i - 1] % MOD;
         }
         
         int second = (input.charAt(first - 1) - '0') * 10 + input.charAt(first) - '0';
         
         if(second >= 10 && second <= 26) {
            dp[i] = (dp[i] + dp[i - 2]) % MOD;
         }
      }
      
      System.out.println(dp[input.length()]);
      bf.close();
   }

}