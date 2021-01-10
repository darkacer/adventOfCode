import { data } from "./data.ts"; 

let user = new data();
// console.log('data is ', user.returnData());

console.log(canArrayAddtwoNums([1,2,3,4,5], 19));
let numIndex = 25;
let startIndex = 0;
for(; numIndex < user.returnData().length; numIndex++) {

    let tempArray = user.returnData().slice(startIndex, numIndex)
    if(!canArrayAddtwoNums(tempArray, user.returnData()[numIndex])) 
        break;
}
console.log(numIndex, user.returnData()[numIndex])


function canArrayAddtwoNums(arrayNum:number[], num:number) : boolean {
    let flag = false
    let count = 0;
    while(!flag && count < arrayNum.length) {
        if(arrayNum.includes(num - arrayNum[count])) {
            flag = true;
        }
        count++
    }
    return flag;
}