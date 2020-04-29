import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Person implements Comparable<Person> {
	int start; // 시작 시간
	int end; // 종료 시간
	int num; // 현재 앉아있는 컴퓨터 좌석 번호.

	Person(int start, int end) {
		this.start = start;
		this.end = end;
	}

	@Override
	public int compareTo(Person o) {
		return end - o.end;
	}

}

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine());

		Person[] people = new Person[N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());

			people[i] = new Person(start, end);
		}

		// 시작 시간이 빠른 순서대로 정렬.
		Arrays.sort(people, new Comparator<Person>() {

			@Override
			public int compare(Person o1, Person o2) {
				return o1.start - o2.start;
			}

		});

		int computer = 0;
		int[] peopleNum = new int[100001];

		// 종료 시간이 빠른 것을 기준으로 우선순위큐 구현.
		PriorityQueue<Person> pq = new PriorityQueue<>();

		for (int i = 0; i < N; i++) {
			if (pq.isEmpty()) { // i = 0인 초기 과정.
				people[i].num = computer; // 현재 앉은 좌석의 번호를 부여. (초기니까 0)
				peopleNum[0] = 1; // 0번 좌석에 인원 수 1.
				computer++; // 컴퓨터 개수 증가.
				pq.offer(people[i]); // 현재 앉은 사람을 우선순위큐에 집어 넣음.
			} else {
				Person person = pq.peek(); // 우선순위큐에서 종료 시간이 가장 빠른 사람.

				// 컴퓨터에 앉으려는 사람이 person보다 시작 시간이 빠르다면, 새로운 컴퓨터를 배정함.
				if (people[i].start < person.end) {
					people[i].num = computer; // 새롭게 배정받은 좌석의 번호를 부여함.
					peopleNum[people[i].num] = 1; // 앉을려는 좌석의 인원수 1.
					computer++; // 컴퓨터 개수 증가.
					pq.offer(people[i]); // 현재 앉은 사람을 우선순위큐에 집어 넣음.

					// 컴퓨터에 앉으려는 사람이 person보다 시작 시간이 늦는다는 얘기는 그 전에 컴퓨터를 이용하던 사람이 떠나갔다는 뜻이므로
					// 가장 최근에 자리에서 떠난 사람의 컴퓨터 좌석을 배정한다.
				} else {
					people[i].num = person.num; // 가장 최근에 자리에서 떠난 사람의 좌석 번호를 부여함.
					peopleNum[people[i].num]++; // 앉을려는 좌석의 인원수를 1 증가시킨다.
					pq.poll(); // 가장 최근에 자리에서 떠났다는 말은 우선순위큐에서 poll()하는 것과 동치.
					pq.offer(people[i]); // 새롭게 자리에 앉은 사람을 우선순위큐에 집어 넣음.
				}
			}
		}

		// 필요한 컴퓨터의 개수.
		bw.write(computer + "\n");

		// 좌석 인원 수.
		for (int i = 0; i < computer; i++) {
			bw.write(peopleNum[i] + " ");
		}
		bw.write("\n");

		bw.flush();
		bw.close();
		br.close();
	}

}
