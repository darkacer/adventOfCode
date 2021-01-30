
import { data } from "./data.ts"; 
let user = new data();
let target = user.returnTarget()

const getNearestDiff = user.getNearestDiff

let inputArr = user.returnArray().filter(el => el != 'x').map(el => parseInt(el))
let outputArr = inputArr.map((el:number) => getNearestDiff(target, el))
let index:number = outputArr.indexOf(Math.min.apply(null,outputArr))

console.log(outputArr[index] * inputArr[index]);
