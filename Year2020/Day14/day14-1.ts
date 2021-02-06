import { data } from "./data.ts"; 
let user = new data();
let inputArr = user.returnArray()
const toBinary = user.toBinary
let answerMap:any = {}

const computeMask = (str:string[], mask:string[]):string => {
    for(let i = 0; i < mask.length; i++) {
        str[i] = (mask[i] !== 'X') ? mask[i] : str[i]
    }
    return str.join('')
}

const applyMask = (mask:string, index:number, value:number):void => {
    answerMap[index] = computeMask(toBinary(value, 36).split(''), mask.split(''));
}

let currentMask = ''

inputArr.forEach(el => {
    let inp = el.split(' = ');
    if(inp[0] === 'mask') {
        currentMask = inp[1];
    } else {
        let index = parseInt(inp[0].replace("mem[", "").replace("]", ""))
        let number = parseInt(inp[1])
        applyMask(currentMask, index, number)
    }
})

const reducer = (acc:number, elem:any):number => acc + parseInt(elem[1], 2)

console.log(Object.entries(answerMap).reduce(reducer, 0));