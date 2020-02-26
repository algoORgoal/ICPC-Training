/*
날짜: 2020-02-23
상태: 맞았습니다!!
*/

/*
    NOTE:
    visited 배열을 사용해서 해당 노드(A)를 탐색했는지 확인하는 이유:
    queue 구조상 데이터는 time이 낮은 순서대로 노드를 꺼내서 접근한다. 따라서 다른 노드(B)에서 이미 방문되었다면 B 노드는 A 노드보다 time이 같거나 작다. 그러므로 
    A 노드로 접근하는 방법은 더이상 시행할 필요가 없다.
*/

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ').map((el) => parseInt(el));
})
    .on('close', function () {
        let result = main(...input);
        console.log(result);
        process.exit();
    })

class Status {
    constructor(position, time) {
        this.position = position;
        this.time = time;
    }

}


let main = function (n, k) {
    let Subin = new Status(0, n);
    let answer = 0;
    let time = 0;
    answer = catchThatCow(n, k, time);
    return answer;
}


let catchThatCow = function (start, end, initialTime) {
    let queue = [];
    let initalStatus = new Status(start, initialTime);
    let visited = Array(100001);

    queue.push(initalStatus);
    while (true) {
        let status = queue.shift();

        if (status.position === end) {
            return status.time;
        } else {
            if (status.position + 1 <= 100000 && !visited[status.position + 1]) {
                queue.push(new Status(status.position + 1, status.time + 1));
                visited[status.position + 1] = true;
            }
            if (status.position - 1 >= 0 && !visited[status.position - 1]) {
                queue.push(new Status(status.position - 1, status.time + 1));
                visited[status.position - 1] = true;
            }
            if (status.position * 2 <= 100000 && !visited[status.position * 2]) {
                queue.push(new Status(status.position * 2, status.time + 1));
                visited[status.position * 2] = true;
            }
        }
    }
}

