#include <iostream>
#include <vector>

using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int dp[2][101][101];
  for (int len = 0; len < 2; len ++) for(int bit = 0; bit < 101; bit++) dp[0][len][bit] = dp[1][len][bit] = 0;
  dp[0][1][0] = 1;
  dp[1][1][0] = 1;
  for(int len = 2; len < 101; len++){
    for(int bit = 0; bit < 101; bit++){
      dp[0][len][bit] = dp[0][len - 1][bit] + dp[1][len - 1][bit];

      dp[1][len][bit] = dp[0][len - 1][bit];
      if(bit > 0) dp[1][len][bit] += dp[1][len - 1][bit - 1];
    }
  }

  int T;
  cin >> T;
  for(int t = 0; t < T; t++){
    int N, K;
    cin >> N >> K;

    int answer = dp[0][N][K] + dp[1][N][K];
    cout << answer << "\n";
  }
}