import { data } from "./data.ts"; 
let user = new data();

let inputArr = user.returnArray().map(el => (el != 'x') ? parseInt(el) : 0)
let num = 0;
let incrementBy = 1;

for(let i = 0; i < inputArr.length; i++) {
    if(i && inputArr[i - 1]) incrementBy *= inputArr[i - 1]
    if(!inputArr[i]) continue
    while(true) {
        num += incrementBy
        if(!((num + i) % inputArr[i])) {
            break
        }
    }
}
console.log(num);