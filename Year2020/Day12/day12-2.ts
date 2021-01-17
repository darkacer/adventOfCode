import { data } from "./data.ts"; 
let user = new data();
const getCharAndValue = user.getCharAndValue;
const sameMap = new Map([
    ['R270', 'L90'],
    ['R90', 'L270'],
    ['R180', 'L180']
])

const cos = (deg:number) => Math.round(Math.cos(deg * Math.PI / 180))
const sin = (deg:number) => Math.round(Math.sin(deg * Math.PI / 180))

function rotate(px:number, py:number, theta:number):any {
    return {
        x: cos(theta) * (px) - sin(theta) * (py),
        y: sin(theta) * (px) + cos(theta) * (py)
    }
}

let inputArr = user.returnData()
let xShip = 0;
let yShip = 0;
// waypoint is relative to ship
let xWayPt = 10;
let yWayPt = 1;
let i = 0;

function rotateWayPoint(input: string, x:number, y:number):any {
    let inputTemp = sameMap.has(input) ? sameMap.get(input) : input;
    let { value } = getCharAndValue('' + inputTemp);
    ({x, y} = rotate(x, y, value))
    
    return {xWayPt:x, yWayPt:y};
}

while(i < inputArr.length) {

    let inputTemp = inputArr[i++]
    
    let { char, value } = getCharAndValue(''+inputTemp);
    switch (char) {
        case 'N':
            yWayPt += value
            break;
        case 'E':
            xWayPt += value
            break;
        case 'S':
            yWayPt -= value
            break;
        case 'W':
            xWayPt -= value
            break;
        case 'F':
            xShip += value * xWayPt
            yShip += value * yWayPt
            break;
        case 'R':
            ({xWayPt, yWayPt} = rotateWayPoint(inputTemp, xWayPt, yWayPt))
            break;
        case 'L':
            ({xWayPt, yWayPt} = rotateWayPoint(inputTemp, xWayPt, yWayPt))
            break;
        default:
            break;
    }
}

console.log(xShip, yShip)
console.log(Math.abs(xShip) + Math.abs(yShip))