/*
    문제 이름: 암호 만들기
    상태: 미완성
*/

const fs = require('fs');
const input = fs.readFileSync('TestJs/stdin').toString().split(/\r\n|\s/);
const countCombi = input.shift();
const countLetter = input.shift();
console.log(input);


function generatePwd(countCombi, letters, passwords) {
    // let password;
    let vowelsAndConsonant;

    checkVowels(password);
    while (true) {

    }
}


function checkVowels(password) {
    let countVowel = 0;
    let countConsonant = 0;

    for (let letter in password) {
        if (/[aeiou]/.match(letter)) {
            countVowel++;
        }
        else {
            countConsonant++;
        }
    }
    return [countVowel, countConsonant];
}



// console.log(input);
