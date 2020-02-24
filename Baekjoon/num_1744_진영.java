package noj.am;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Collections;
import java.util.Vector;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int N = Integer.parseInt(br.readLine()); // 입력할 값 개수
		Vector<Integer> pv = new Vector<>(); // 양수 집합
		Vector<Integer> zv = new Vector<>(); // 0 집합
		Vector<Integer> nv = new Vector<>(); // 음수 집합

		for (int i = 0; i < N; i++) { // 입력
			int num = Integer.parseInt(br.readLine());
			if (num > 0) {
				pv.add(num);
			} else if (num == 0) {
				zv.add(num);
			} else {
				nv.add(num);
			}
		}
		Collections.sort(pv); // 양수는 내림차순 정렬
		Collections.sort(nv, Collections.reverseOrder()); // 음수는 오름차순 정렬

		int[] nums = new int[N - zv.size()]; // 0을 제외한 값들을 하나로 합칠 배열

		// 0을 제외한 나머지 값들을 각각 넣어 줌.
		for (int i = 0; i < nv.size(); i++) {
			nums[i] = nv.get(i);
		}

		for (int i = nv.size(); i < N - zv.size(); i++) {
			nums[i] = pv.get(i - nv.size());
		}

		int ans = 0;
		for (int i = N - zv.size() - 1; i >= 0; i--) {
			if (nums[i] > 0) { // 양수일 경우
				if (i - 1 >= 0) {
					if (nums[i - 1] > 1) { // 1보다 클 때는 두 수를 곱해서 ans에 더해 줌.
						ans += nums[i] * nums[i - 1];
						i--;
					} else { // 그렇지 않을 경우, nums[i]만 ans에 더해 줌.
						ans += nums[i];
					}
				} else {
					ans += nums[i];
				}
			} else { // 음수일 경우
				if (nv.size() % 2 == 0) { // 음수의 개수가 짝수 개일 경우
					ans += nums[i] * nums[i - 1]; // 음수2 개를 곱해서 ans에 더해 줌.
					i--;
				} else { // 음수의 개수가 홀수 개일 경우
					if (zv.size() != 0) { // 0의 개수가 0개가 아닐 경우
						if (i == 0) { // 맨 처음에 오는 음수를 0이랑 곱해서 지워주어야 함.
							break;
						} else { // 그렇지 않을 경우, 음수 2개를 곱해서 ans에 더해 줌.
							ans += nums[i] * nums[i - 1];
							i--;
						}
					} else { // 0의 개수가 0개일 경우
						if (i == 0) { // 음수랑 0이랑 곱해서 상쇄할 방법이 없으므로 그냥 더해 줌.
							ans += nums[i];
						} else { // 그렇지 않을 경우 음수 2개를 곱해서 ans에 더해 줌.
							ans += nums[i] * nums[i - 1];
							i--;
						}
					}
				}
			}
		}

		bw.write(ans + "\n");
		bw.flush();
		bw.close();
		br.close();
	}

}
