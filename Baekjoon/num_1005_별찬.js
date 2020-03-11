/*
문제: ACM CRAFT
상태: 미완성
작성 날짜: March 7, 2020
*/

// 만족시키지 못한 조건
// 1. 목표 건물이 있는 그래프를 찾아낸다.
// 2. 찾아낸 그래프의 처음 노드부터 탐색을 시작한다.

// const fs = require('fs');
// const fs = require('fs');
// const input = fs.readFileSync('TestJS/stdin').toString().split(/\s|\r\n/).map((el) => parseInt(el));

// const input = fs.readFileSync('TestJs/stdin').toString().split(/\s|\r\n/).map((el) => parseInt(el));
// const input = fs.readFileSync('dev/stdin').toString().split(/\s|\r\n/).map((el) => parseInt(el));

const fs = require('fs');
const input = fs.readFileSync('TestJs/stdin').toString().split(/\r\n|\s/).map((el) => parseInt(el));

const countTestCase = input.shift();

function main(input) {
    const countBuilding = input.shift(); // 건물의 개수
    const countOrder = input.shift(); // 건설순서규칙 개수
    let constructionTimeArr = [];
    let buildingGraphObj = {};

    let start; //시작 지점
    for (let i = 0; i < countBuilding; i++) {
        constructionTimeArr.push(input.shift());
        buildingGraphObj[(i + 1)] = [];
    }
    for (let i = 0; i < countOrder; i++) {
        let key = input.shift();
        let value = input.shift();
        buildingGraphObj[key].push(value);
    }
    let target = input.shift();
    let visited = Array(countBuilding);
    visited.fill(false);


    // console.log(countBuilding);
    // console.log(countOrder);
    // console.log(constructionTimeArr);
    // console.log(buildingGraphObj);
    // console.log(target);
    // console.log('\n');
    // let result = solveACMCraft(constructionTimeArr, buildingGraphObj, target, 0, 1, visited);
    console.log(buildingGraphObj);
    parentNodes = [];
    let rootNode = getNodesWithNoParent(buildingGraphObj, target, parentNodes);

    console.log(`rootNode:${rootNode}`);

    // console.log(`result: ${result}`);
}

// function findStart(constructionTimeArr, buildingGraphObj, target, )
function getNodesWithNoParent(dagObj, childNode, nodesWithNoParent) {
    /*
    1 -> 2 -> 3 -> 4 -> 5
    1: [2], 2: [3], 4:[5]
    */

    for (let key in dagObj) {
        for (let node of dagObj[key]) {
            if (node === childNode) {
                // console.log(`key:${key}`);
                // console.log(`node:${node}`);
                getNodesWithNoParent(dagObj, parseInt(key));
            }
        }
    }
    return nodesWithNoParent; //if parent node can't be found
}



function solveACMCraft(createTimeArr, buildingsObj, target, time, currentBuilding, visited) {
    time += createTimeArr[currentBuilding - 1];
    visited[currentBuilding - 1] = true;
    let nextBuildingArr = buildingsObj[currentBuilding];
    // console.log(`nextBuildingArr: ${nextBuildingArr}`);
    // console.log(`time: ${time}`);
    if (target === currentBuilding) { //1과 해당 원소가 이어져있다고 가정할 때 가능한 조건식.

        return createTimeArr[target - 1];
    }
    let nextMaxTime = 0;
    for (let building of nextBuildingArr) {
        let nextTime = solveACMCraft(createTimeArr, buildingsObj, target, 0, building, visited);
        if (nextMaxTime < nextTime) {
            nextMaxTime = nextTime;
        }
    }
    // console.log(`return value:${time + nextMaxTime}`);
    return time + nextMaxTime;
}

for (let i = 0; i < countTestCase; i++) {
    main(input);
}

// console.log(input);


