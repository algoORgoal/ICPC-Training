/*
    문제 이름: 블랙잭
    상태: 완성
    날짜: 2020-03-13
*/




const fs = require('fs');
// let input = fs.readFileSync('TestJs/stdin').toString().split(/\r\n|\s/).map((el) => parseInt(el));
let input = fs.readFileSync('dev/stdin').toString().split(/\r\n|\s|\n/).map((el) => parseInt(el));

n = input.shift();
m = input.shift();


cards = [];


for (let i = 0; i < n; i++) {
    let data = input.shift();
    cards.push(data);
}


let combination = 1000000;
for (let i = 0; i < cards.length; i++) {
    for (let j = i + 1; j < cards.length; j++) {
        for (let k = j + 1; k < cards.length; k++) {
            let temp = cards[i] + cards[j] + cards[k];
            if (temp === m) {
                combination = m;
                break;
            }
            else if (temp < m && Math.abs(m - temp) < Math.abs(m - combination)) {
                combination = temp;
            }
        }
    }
}
console.log(combination);

