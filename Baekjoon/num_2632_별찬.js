/*
    날짜: 2020 - 02 - 28
    상태: 미완성
    문제 이름: 피자판매
*/
const fs = require('fs');
const input = fs.readFileSync('TestJs/stdin').toString().split(/\r\n|\s/).map((el) => parseInt(el));
// const input = fs.readFileSync('dev/stdin').toString().split(/\r\n|\s/).map((el) => parseInt(el));
console.log(input);

const size = input.shift();
const m = input.shift();
const n = input.shift();

let sliceA = [];
for (let i = 0; i < m; i++) {
    sliceA.push(input.shift());
}

let sliceB = [];
for (let i = 0; i < n; i++) {
    sliceB.push(input.shift());
}


function LinkedList() {
    var length = 0;
    var head = null;

    var Node = function (element) {
        this.element = element;
        this.next = null;
    };

    this.head = function () {
        return head;
    };

    this.add = function (element) {
        var newNode = new Node(element);
        if (length === 0) {
            head = newNode;
            length++;
        }
        else if (length === 1) {
            var node = head;
            head.next = newNode;
            newNode.next = head;
            length++;
        }
        else {
            var node = head;
            currentIndex = 0;
            while (currentIndex < length - 1) {
                node = node.next;
                currentIndex++;
            }
            node.next = newNode;
            newNode.next = head;
            length++;
        }

    };


    this.print = function () {
        node = head;
        currentIndex = 0;
        console.log('start');
        while (currentIndex < length) {
            console.log(node.element);
            node = node.next;
            currentIndex++;
        }
        console.log('end');
    };

    this.findSlices = function (servings) {
        let currendIndex = 0;
        let sum = 0;
        let node = head;
        let chances = 0;

        while (sum < servings) {
            sum += node.element;
            console.log(sum);
            if (sum === servings) {
                console.log("걸렸다!");
                console.log(chances);
                chances++;
                break;
            }
            node = node.next;
        }
    }
}

var pizzaA = new LinkedList();
sliceA.forEach((el, index) => {
    pizzaA.add(el);
});

pizzaA.print();
pizzaA.findSlices(7);