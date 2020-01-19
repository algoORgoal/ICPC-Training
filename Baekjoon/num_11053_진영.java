/*
#2020년 1월 17일
#박진영, java
#11053번 문제
#타뷸레이션
*/

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class num_11053_진영 {
   public static void main(String[] args) throws NumberFormatException, IOException {
      BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
      BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
      int N = Integer.parseInt(bf.readLine());
      int[] sequence = new int[1001]; // 수열
      int[] dp = new int[1001]; // 임시 길이
      
      StringTokenizer st = new StringTokenizer(bf.readLine());
      for (int i = 1; i <= N; i++) {
         int temp = Integer.parseInt(st.nextToken());
         sequence[i] = temp;
      }
      
      dp[1] = 1;
      int length = 1; // 최종 길이
      for(int i = 2; i <= N; i++) {
         dp[i] = 1;
         
         for(int j = 1; j < i; j++) {
            if(sequence[i] > sequence[j] && dp[i] <= dp[j]) {
               // 하나의 요소가 그 전꺼보다 크고, dp 값이 최대로만 초기화되어야함.
               // 예를 들어, 10 20 10 30 에서 sequence[i]=30일 경우를 생각해 보자.
               // dp는 1, 2, 1인 상태이다.
               // 그러면, dp[4]는 2->3->2가 될 것이다. 이 때, && 뒤에 조건식을 추가함으로써
               // 3->2로 초기화되는 현상을 막을 수 있다.
               dp[i] = dp[j] + 1;
            }
         }
         length = Math.max(length, dp[i]);
      }
      
      bw.write(length + "\n");
      bw.flush();
      bw.close();
      bf.close();
   }

}