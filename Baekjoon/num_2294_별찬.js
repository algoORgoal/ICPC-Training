/*
    날짜: 2020 - 02 - 28
    상태: 완성(정답)
    문제 이름: 동전 1
*/

const fs = require('fs');
const input = fs.readFileSync('TestJs/stdin').toString().split(/\r\n|\s/).map((el) => parseInt(el));
// const input = fs.readFileSync('dev/stdin').toString().split(/\r\n|\s/).map((el) => parseInt(el));
console.log(input);
main(...input);

function main(n, k, ...coins) {
    console.log(coins);
    coins.sort((coin1, coin2) => coin2 - coin1);
    const coinSet = new Set(coins);
    console.log(coinSet);
}
