package noj.am;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

class ListNode { // 노드
	long value;
	ListNode next;

	ListNode(long value, ListNode next) {
		this.value = value;
		this.next = next;
		this.next = null;
	}
}

class CircularList { // 원형링크드리스트
	ListNode CL;

	CircularList() {
		this.CL = null;
	}

	// 마지막 노드에 삽입
	void insertLastNode(long value) {
		ListNode node = new ListNode(value, null);
		if (CL == null) {
			CL = node;
			node.next = node;
		} else {
			ListNode current = CL;
			while (current.next != CL) {
				current = current.next;
			}
			node.next = current.next;
			current.next = node;
		}
	}

	ListNode searchNode(long value) {
		ListNode node = new ListNode(value, null);
		if (CL == null) {
			return null;
		} else {
			ListNode current = CL;
			while (current.value != node.value) {
				current = current.next;
			}
			return current;
		}
	}
}

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		long T = Long.parseLong(br.readLine());

		StringTokenizer st = new StringTokenizer(br.readLine());
		long m = Long.parseLong(st.nextToken());
		long n = Long.parseLong(st.nextToken());

		CircularList A = new CircularList();
		CircularList B = new CircularList();

		for (long i = 0; i < m; i++) {
			long temp = Long.parseLong(br.readLine());
			A.insertLastNode(temp);
		}

		for (long i = 0; i < n; i++) {
			long temp = Long.parseLong(br.readLine());
			B.insertLastNode(temp);
		}

		Map<Long, Long> map = new HashMap<>();

		ListNode node = A.CL;
		for (long i = 0; i < m; i++) {
			long sum = 0;
			ListNode temp = node;

			if (i == 0) {
				for (long j = 0; j < m; j++) {
					sum += temp.value;
					if (map.containsKey(sum)) {
						map.put(sum, map.get(sum) + 1);
					} else {
						map.put(sum, (long) 1);
					}
					temp = temp.next;
				}
			} else {
				for (long j = 0; j < m - 1; j++) {
					sum += temp.value;
					if (map.containsKey(sum)) {
						map.put(sum, map.get(sum) + 1);
					} else {
						map.put(sum, (long) 1);
					}
					temp = temp.next;
				}
			}
			node = node.next;
		}

		long ans = 0;

		if (map.containsKey(T)) {
			ans += map.get(T);
		}

		node = B.CL;
		for (long i = 0; i < n; i++) {
			long sum = 0;
			ListNode temp = node;

			if (i == 0) {
				for (long j = 0; j < n; j++) {
					sum += temp.value;
					if (map.containsKey(T - sum)) {
						ans += map.get(T - sum);
					}

					if (sum == T) {
						ans++;
					}
					temp = temp.next;
				}
			} else {
				for (long j = 0; j < n - 1; j++) {
					sum += temp.value;
					if (map.containsKey(T - sum)) {
						ans += map.get(T - sum);
					}

					if (sum == T) {
						ans++;
					}
					temp = temp.next;
				}
			}
			node = node.next;
		}

		bw.write(ans + "\n");
		bw.flush();
		bw.close();
		br.close();
	}

}
