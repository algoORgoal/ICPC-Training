const fs = require('fs');
const input = fs.readFileSync('TestJs/stdin').toString().split(/\r\n|\s/).map((el) => parseInt(el));
console.log(input);

const amount = input.shift();
const countType = input.shift();

let dp = Array(amount);
dp.fill(0);



let coins = {};
for (let i = 0; i < input.length; i += 2) {
    coins[input[i]] = input[i + 1];
}

console.log(coins);

while (true) {
    const copy = [...dp];
    let a = 0;
    for (let coin in coins) {

    }
}





/*
function solveCoins(coinObj, tempObj, amount, result, index) {
    for (coin in coinObj) {
        if (amount % coinObj[coin] == 0) {
            return
        }
    }

    // if (amount === 0) {

    // }
    // for (let coin of coinObj) {

    // }
    // if (amount === countCoins[index] * coins[index]) {

    // }
    // else if (amount > countCoins[index] * coins[index]) {
    //     if (solveCoins(coins, countCoins, amount - countCoins * coins, result){ }
    // }
    // else if (amount < countCoins[index] * coins[index]) { }

}


console.log(coins);
console.log(countCoins);
console.log(coins);
*/