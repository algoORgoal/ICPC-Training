/*
날짜: 2020-02-23
상태: 미완성
*/

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = 0;
let exponent = 0;
let result = ``;


rl.on('line', function (line) {
    // input = line.split(' ').map((el) => parseInt(el));
    input = line;
    exponent = main(input);
    result = draw(exponent);
})
    .on('close', function () {
        console.log(result);
        process.exit();
    });

let main = function (input) {
    let exponent = 0;
    while (input >= 1) {
        console.log(`current input: ${input}`);
        input /= 3;
        exponent++;
    }
    exponent--;
    return exponent;
}

let draw = function (n) {
    let unit = '*';
    let temp;
    for (let i = 0; i < n; i++) {
        unit = `${unit}${unit}${unit}\n${unit} ${unit}\n${unit}${unit}${unit}\n`;
    }
    return unit;
}