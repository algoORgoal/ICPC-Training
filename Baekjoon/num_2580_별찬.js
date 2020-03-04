/*
    문제 이름: 스도쿠
    상태: 미완성
    기록일: March 2, 2020
*/



const fs = require('fs');
const input = fs.readFileSync('TestJs/stdin').toString().split(/\r\n|\s/).map((el) => parseInt(el));
console.log(input);


const row = 9;
const col = 9;

let table = [];
for (let i = 0; i < row; i++) {
    let arr = [];
    for (let j = 0; j < col; j++) {
        arr.push(input.shift());
    }
    table.push(arr);
}

const digits = [1, 2, 3, 4, 5, 6, 7, 8, 9];

let notInEachRow = []
let notInEachCol = [];
let notInSquare = [];

let emptyPosition = [];


for (let i = 0; i < col; i++) {
    let hidden = table[i].reduce((notInRow, currentNum) => {

        if (currentNum !== 0) {
            const index = notInRow.indexOf(currentNum);
            return notInRow.slice(0, index).concat(notInRow.slice(index + 1));
        } else {
            return notInRow;
        }
    }, [1, 2, 3, 4, 5, 6, 7, 8, 9]);
    notInEachRow.push(hidden);
}
console.log(notInEachRow);

for (let i = 0; i < row; i++) {
    let colArr = [];
    for (let j = 0; j < col; j++) {
        colArr.push(table[j][i]);
    }

    let hidden = colArr.reduce((notInCol, currentNum) => {
        if (currentNum !== 0) {
            const index = notInCol.indexOf(currentNum);
            return notInCol.slice(0, index).concat(notInCol.slice(index + 1));
        } else {
            return notInCol;
        }
    }, [1, 2, 3, 4, 5, 6, 7, 8, 9]);
    notInEachCol.push(hidden);
}
console.log(notInEachCol);

squareRange1 = [0, 1, 2];
squareRange2 = [0, 1, 2];
squareRange3 = [0, 1, 2];

squareRange2.reduce(() => {
    squareRange1.reduce((cur, el) => {
        return cur;
    }, []);
    squareRange1.map((el) => el + 3);
}, []);



for (let i = 0; i < col; i++) {
    let hidden = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    for (let j = Number.parseInt(i / 3) * 3; j < Number.parseInt(i / 3) * 3 + 3; j++) {
        for (let k = i % 3 * 3; k < i % 3 * 3 + 3; k++) {
            if (table[j][k] !== 0) {
                let index = hidden.indexOf(table[j][k]);
                hidden.splice(index, 1);
            } else {
                emptyPosition.push([j, k]);
            }
        }
    }
    notInSquare.push(hidden);
}
console.log(notInSquare);
console.log(emptyPosition);

for (let i in emptyPosition) {

}