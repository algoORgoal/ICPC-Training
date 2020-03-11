/*
    날짜: 2020 - 02 - 28
    상태: 미완성
    문제 이름: 동전 1
*/

const fs = require('fs');
const input = fs.readFileSync('TestJs/stdin').toString().split(/\r\n|\s|\n/).map((el) => parseInt(el));
// const input = fs.readFileSync('dev/stdin').toString().split(/\r\n|\s/).map((el) => parseInt(el));
console.log(input);
main(...input);

function main(n, k, ...coins) {
    console.log(coins);
    coins.sort((coin1, coin2) => coin1 - coin2); //sort in ascendant order
    const coinSet = new Set(coins);
    console.log(coinSet);
    let array = Array(16);
    array.fill(0);
    console.log(`initial: ${array}`);
    find_coins(15, [1, 5, 12], array, 12);
    console.log(`result: ${array}`);
}

function find_coins(n, arr, cost, leastValue) {
    console.log(cost);
    if (n in arr) {
        return 1;
    }
    if (n < arr[0]) {
        return -500; //unable to sum up the coins
    }
    else {
        /*
        for (let i = arr.length - 1; i >= 0; i--) {
            if (arr[i] < n) {
                if (cost[n - arr[i]] == 0) {
                    cost[n - arr[0]] = 1 + recursion(n - arr[0], arr, cost);
                }
            }
        }
        */

        if (arr[2] < n && arr[2] <= leastValue) {
            console.log(1);
            if (cost[n - arr[2]] === 0) {
                cost[n] = 1 + find_coins(n - arr[2], arr, cost, arr[2]);
            } else {
                cost[n] = 1 + cost[n - arr[2]];
            }
        }
        if (arr[1] < n && arr[1] <= leastValue) {
            console.log(2);
            if (cost[n - arr[1]] === 0) {
                cost[n] = 1 + find_coins(n - arr[1], arr, cost, arr[1]);
            } else {
                cost[n] = 1 + cost[n - arr[1]];
            }
        }
        if (arr[0] < n && arr[0] <= leastValue) {
            console.log(3);
            if (cost[n - arr[0]] === 0) {
                cost[n] = 1 + find_coins(n - arr[0], arr, cost, arr[0]);
            } else {
                cost[n] = 1 + cost[n - arr[0]];
            }
        }
    }
}