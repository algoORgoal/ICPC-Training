public class num_1517_진영 {
    public static long swap = 0;
    public static long[] tmp; // 병합정렬 내부에서 사용될 배열

    public static void main(String[] args) throws NumberFormatException, IOException {
        // TODO Auto-generated method stub
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(bf.readLine());
        tmp = new long[N];
        long[] arr = new long[N];

        String input = bf.readLine();
        StringTokenizer st = new StringTokenizer(input);

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        MergeSort(arr, 0, N - 1); // 병합 정렬

        bw.write(swap + "\n");
        bf.close();
        bw.close();
    }

    public static void MergeSort(long[] arr, int p, int r) { // 분할
        if (p < r) {
            int q = (p + r) / 2;
            MergeSort(arr, p, q);
            MergeSort(arr, q + 1, r);
            Merge(arr, p, q, r);
        }
    }

    public static void Merge(long[] arr, int p, int q, int r) { // 정복
        int i = p, j = q + 1, k = p;
        // 여기서 int long[] tmp = new long[arr.length] 하면 시간 초과남.

        while (i <= q && j <= r) { // 예를 들어, p부터 q는 2 3, q+1부터 r까지는 1이 있다고 가정하자.
            if (arr[i] <= arr[j]) {
                tmp[k++] = arr[i++];
            } else { // 이때, arr[i] > arr[j]이므로 이 쪽으로 오게 된다.
                tmp[k++] = arr[j++];
                swap += (q + 1 - i); // arr[j]보다 큰 값인 2와 3이 swap의 횟수가 된다. (즉, arr[j]보다 arr[i]의 큰 개수가 몇 개인지 계산)
            }
        }

        while (i <= q) {
            tmp[k++] = arr[i++];
        }

        while (j <= r) {
            tmp[k++] = arr[j++];
        }

        for (i = p; i <= r; i++) {
            arr[i] = tmp[i];
        }

    }

}