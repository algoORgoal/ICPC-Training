
/*
문제: 신입 사원
상태: 미완성
거리가 먼 것부터 제거
*/



const fs = require('fs');
const input = fs.readFileSync('TestJs/stdin').toString().split(/\r\n|\s/).map((el) => parseInt(el));
const countCase = input.shift();

for (let i = 0; i < testCase; i++) {

}

const countStudent = input.shift();
let map = [];
for (let j = 0; j < countStudent; j++) {
    const paper = input.shift();
    const interview = input.shift();
    map.push([paper, interview, Math.abs(paper - interview)]);
}
console.log(map);



