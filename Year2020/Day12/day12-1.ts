import { data } from "./data.ts"; 

let user = new data();

let inputArr = user.returnData()

const directions = ['N', 'E', 'S', 'W'];
const getCharAndValue = user.getCharAndValue;

function switcher(x:number, y:number, input:string, currentDirection:number):any {
    let {char, value} = getCharAndValue(input);
    switch (char) {
        case 'N':
            y += value
            break;
        case 'E':
            x += value
            break;
        case 'S':
            y -= value
            break;
        case 'W':
            x -= value
            break;
        case 'L':
            currentDirection = updateDirection(currentDirection, input);
            break;
        case 'R':
            currentDirection = updateDirection(currentDirection, input);
            break;
        case 'F':
            ({x, y, currentDirection} = switcher(x,y, directions[currentDirection] + value, currentDirection))
            break;
    }
    return {x: x, y: y, currentDirection: currentDirection}
}



function updateDirection(currentDirection: number, update: string) : number {
    
    let {char, value} = getCharAndValue(update);
    if(char === 'R' && value === 90) currentDirection = (currentDirection + 5) % 4
    if(char === 'L' && value === 270) currentDirection = (currentDirection + 5) % 4
    if(char === 'R' && value === 180) currentDirection = (currentDirection + 6) % 4
    if(char === 'L' && value === 90) currentDirection = (currentDirection + 3) % 4
    if(char === 'R' && value === 270) currentDirection = (currentDirection + 3) % 4
    if(char === 'L' && value === 180) currentDirection = (currentDirection + 2) % 4
    
    return currentDirection
}

let i = 0;
let x = 0;
let y = 0;
let currentDirection = 1;

while(i < inputArr.length) {
    ({x, y, currentDirection} = switcher(x, y, inputArr[i], currentDirection))
    i++
}

console.log(x, y);
console.log(Math.abs(x) + Math.abs(y))
