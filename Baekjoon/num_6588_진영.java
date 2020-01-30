public class num_6588_진영 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        // TODO Auto-generated method stub
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String input = "";
        final int MAX = 1000000;
        boolean[] primeList = new boolean[MAX + 1]; // 소수인지 판별. (에라토스테네스의 체)

        for (int i = 2; i <= MAX; i++) {
            primeList[i] = true;
        }

        for (int i = 2; i * i <= MAX; i += 1) { // 소수와 합성수 구별하는 과정
            for (int j = i * i; j <= MAX; j += i) {
                primeList[j] = false;
            }
        }

        outer: while (!(input = bf.readLine()).equals("0")) {
            int N = Integer.parseInt(input);

            if (N % 2 != 0) { // 홀수인 경우 예외.
                bw.write("Goldbach's conjecture is wrong.\n");
                bw.flush();
                continue outer;
            }

            for (int i = 3; i <= N; i += 2) { // i + (N - i) = N이 되어야 함.
                if (primeList[i] && primeList[N - i]) {
                    bw.write(N + " = " + i + " + " + (N - i) + "\n");
                    bw.flush();
                    continue outer;
                }
            }
        };

        bf.close();
        bw.close();
    }

}