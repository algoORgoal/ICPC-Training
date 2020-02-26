/*
날짜: 2020-02-23
상태: 틀렸습니다(67%)
*/

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];



rl.on('line', function (line) {
    // input = line.split(' ').map((el) => parseInt(el));
    input = line.split(' ').map((el) => parseInt(el));
})
    .on('close', function () {
        let answer = main(...input);
        console.log(answer);
        process.exit();
    });

let main = function (n, m) {
    let answer;
    let count = 1;
    let coord = [1, 1]

    if (n == 1 || m == 1) {
        answer = 1;
    }
    else if (n <= 2) {
        while (true) {
            if (coord[1] < m - 1) {
                move_two(coord);
                count++;
            } else {
                return count;
            }
            if (coord[1] < m - 1) {
                move_three(coord);
                count++;
            }
            else {
                return count;
            }
            if (coord[1] < m - 1) {
                move_two(coord);
                count++;
            } else {
                return count;
            }
            if (coord[1] < m - 1) {
                move_three(coord);
                count++;
            }
            else {
                return count;
            }
        }
    } else if (n >= 3) {
        if (coord[1] < m) {

            move_one(coord);
            count++;
        } else {
            return count;
        }
        if (coord[1] < m) {

            move_four(coord);
            count++;
        } else {
            return count;
        }
        if (coord[1] < m) {

            move_one(coord);
            count++;
        } else {
            return count;
        }
        if (coord[1] < m - 4) {
            if (coord[1] < m) {

                move_four(coord);
                count++;
            } else {
                return count;
            }
            if (coord[1] < m - 1) {

                move_two(coord);
                count++;
            } else {
                return count;
            }
            if (coord[1] < m - 1) {

                move_three(coord);
                count++;
            } else {
                return count;
            }

            while (true) {
                if (coord[1] < m) {

                    move_one(coord);
                    count++;
                } else {
                    return count;
                }
                if (coord[1] < m) {
                    move_four(coord);
                    count++;
                }
                else {
                    return count;
                }
            }
        }
    }
    return count;
}


let move_one = function (coord) {
    coord[0] += 2;
    coord[1] += 1;
}


let move_two = function (coord) {
    coord[0] += 1;
    coord[1] += 2;
}

let move_three = function (coord) {
    coord[0] -= 1;
    coord[1] += 2;
}

let move_four = function (coord) {
    coord[0] -= 2;
    coord[1] += 1;
}