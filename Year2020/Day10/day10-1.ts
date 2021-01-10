import { data } from "./data.ts"; 

let user = new data();
let chargingOutlet = 0;
let oneJumpCount = 0;
let threeJumpCount = 1;
let temp = 0;
user.returnData().sort((a, b) => a - b).forEach(element => {
    if(element - temp === 1) {
        oneJumpCount++
        // temp = element
    } else if(element - temp === 3) {
        threeJumpCount++
        // temp = element
    }
    temp = element
});

console.log('year ' , threeJumpCount * oneJumpCount)