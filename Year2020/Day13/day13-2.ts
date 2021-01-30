import { data } from "./data.ts"; 
let user = new data();

const getNearestDiff = user.getNearestDiff
// let target = user.returnTarget()
// let inputArr = user.returnArray().map(el => (el != 'x') ? parseInt(el) : 0)

let inputArr = [7,13,0,0,59,0,31,19]

let biggestindex:number = inputArr.indexOf(Math.max.apply(null,inputArr))


// let multipler = 1000001163389
let multipler = 1
let num = inputArr[biggestindex]
while(true) {
    num = inputArr[biggestindex] * multipler++ - biggestindex
    console.log(multipler);
    
    let innerFlag = true
    for(let i = 0; i < inputArr.length; i++) {

        if(!inputArr[i]) continue;
        // console.log(num, inputArr[i], getNearestDiff(num, inputArr[i]));
        
        if(getNearestDiff(num, inputArr[i]) !== i) {
            innerFlag = false
            break
        }
    }
    if(innerFlag) break;
}

console.log('num', num);
