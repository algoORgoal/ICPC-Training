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

		int N = Integer.parseInt(br.readLine()); // �Է��� �� ����
		Vector<Integer> pv = new Vector<>(); // ��� ����
		Vector<Integer> zv = new Vector<>(); // 0 ����
		Vector<Integer> nv = new Vector<>(); // ���� ����

		for (int i = 0; i < N; i++) { // �Է�
			int num = Integer.parseInt(br.readLine());
			if (num > 0) {
				pv.add(num);
			} else if (num == 0) {
				zv.add(num);
			} else {
				nv.add(num);
			}
		}
		Collections.sort(pv); // ����� �������� ����
		Collections.sort(nv, Collections.reverseOrder()); // ������ �������� ����

		int[] nums = new int[N - zv.size()]; // 0�� ������ ������ �ϳ��� ��ĥ �迭

		// 0�� ������ ������ ������ ���� �־� ��.
		for (int i = 0; i < nv.size(); i++) {
			nums[i] = nv.get(i);
		}

		for (int i = nv.size(); i < N - zv.size(); i++) {
			nums[i] = pv.get(i - nv.size());
		}

		int ans = 0;
		for (int i = N - zv.size() - 1; i >= 0; i--) {
			if (nums[i] > 0) { // ����� ���
				if (i - 1 >= 0) {
					if (nums[i - 1] > 1) { // 1���� Ŭ ���� �� ���� ���ؼ� ans�� ���� ��.
						ans += nums[i] * nums[i - 1];
						i--;
					} else { // �׷��� ���� ���, nums[i]�� ans�� ���� ��.
						ans += nums[i];
					}
				} else {
					ans += nums[i];
				}
			} else { // ������ ���
				if (nv.size() % 2 == 0) { // ������ ������ ¦�� ���� ���
					ans += nums[i] * nums[i - 1]; // ����2 ���� ���ؼ� ans�� ���� ��.
					i--;
				} else { // ������ ������ Ȧ�� ���� ���
					if (zv.size() != 0) { // 0�� ������ 0���� �ƴ� ���
						if (i == 0) { // �� ó���� ���� ������ 0�̶� ���ؼ� �����־�� ��.
							break;
						} else { // �׷��� ���� ���, ���� 2���� ���ؼ� ans�� ���� ��.
							ans += nums[i] * nums[i - 1];
							i--;
						}
					} else { // 0�� ������ 0���� ���
						if (i == 0) { // ������ 0�̶� ���ؼ� ����� ����� �����Ƿ� �׳� ���� ��.
							ans += nums[i];
						} else { // �׷��� ���� ��� ���� 2���� ���ؼ� ans�� ���� ��.
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
