//문제 이름: 좌표 압축
//상태: 해결
//작성 일자: 2020-04-10

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const coord = input[1].split(' ').map((el) => parseInt(el));
const coordMap = quickSort(coord).reduce(addProperty, {});
const answer = coord.map(press).reduce(print, '');
console.log(answer);

function quickSort(arr) {
  if (arr.length === 0) return [];
  const [first, ...elements] = arr;
  const left = elements.filter((el) => el < first);
  const right = elements.filter((el) => el > first);
  return [...quickSort(left), first, ...quickSort(right)];
}

function addProperty(currentObj, currentKey, currentValue) {
  currentObj[currentKey] = currentValue;
  return currentObj;
}

function press(currentKey) {
  return coordMap[currentKey];
}

function print(currentStr, currentNum) {
  return currentStr.concat(`${currentNum} `);
}
