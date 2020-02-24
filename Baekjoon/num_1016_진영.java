import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws NumberFormatException, IOException {
        // TODO Auto-generated method stub
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        long min = Long.parseLong(st.nextToken());
        long max = Long.parseLong(st.nextToken());

        boolean[] arr = new boolean[1000001];

        for (long i = 2; (i * i) <= max; i++) {
            long square = i * i;
            long start = (((min - 1) / square) + 1) * square;

            for (long j = start; j <= max; j += square) {
                arr[(int) (j - min)] = true;
            }
        }

        int ans = 0;
        for (long i = 0; i < max - min + 1; i++) {
            if (arr[(int) i]) {
                ans++;
            }
        }

        bw.write((max - min + 1 - ans) + "\n");
        bw.flush();
        bw.close();
        br.close();
    }

}