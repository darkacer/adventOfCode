import { data } from "./data.ts"; 
let user = new data();
let inputArr = user.returnArray()

const toBinary = user.toBinary
let answerMap:any = {}

const getAllPossibleCombi = (inputStr: string):string[] => {
    let allStrings:string[] = [''];
    inputStr.split('').forEach((ch:string, index:number) => {
        allStrings.forEach((str:string, j:number) => {
            if(index === str.length) {
                if(ch === 'X') {
                    let temp = str
                    allStrings[j] += 1
                    allStrings.push(temp + '0')
                } else {
                    allStrings[j] += ch
                }
            }
        })
    })
    return allStrings;
}

const applyBitMasking = (str:string[], mask:string[]) : string => {
    for(let i = 0; i < str.length; i++) {
        str[i] = (mask[i] != '0') ? mask[i] : str[i]
    }
    return str.join('');
}

const applyMask = (mask:string, index:number, number:number):void => {
    let newMask = applyBitMasking(toBinary(index).split(''), mask.split(''))
    getAllPossibleCombi(newMask).forEach(el => {
        let toIndex = parseInt(el, 2)
        answerMap[toIndex] = number
    })

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
});

const reducer = (acc:number, elem:any):number =>  acc + elem[1]
console.log(Object.entries(answerMap).reduce(reducer, 0));