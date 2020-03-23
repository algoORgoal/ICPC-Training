


const fs = require('fs');
const input = fs.readFileSync('TestJs/stdin').toString().split(/\r\n|\s/).map((el) => parseInt(el));
console.log(input);
const countVertex = input.shift();
const countQuery = input.shift();

let adjacencyList = {};


for (let i = 0; i < countVertex; i++) {
    let start = input.shift();
    let end = input.shift();
    let length = input.shift();
    if (adjacencyList[start]) {
        adjacencyList[start].push([end, length, i]);
    }
    else {
        adjacencyList[start] = [[end, length, i]];
    }
}

console.log(adjacencyList);


for (let i = 0; i < countQuery; i++) {
    let index = input.shift();
    if (index === 1) {

    }
    else {

    }
}

function changeLength(k, x) {
    for (let vertex in adjacencyList) {
        if (adjacencyList[vertex][2] === k - 1) {
            adjacencyList[vertext][1] = x;
        }
    }
}

function findLongestPath(graph, start) {
    // graph[start] = ;
}







