import { data } from "./data.ts"; 

let user = new data();

let input2D = user
        .returnData()
        .map((el:string) => el.split(''))

function applyRules(jsString:string) : any {
    console.log('jsarray')
    let flagDirty = false;
    let inputArr = JSON.parse(jsString);
    let tempArr = JSON.parse(jsString);
    for(let i = 0; i < inputArr.length; i++) {
        for(let j = 0; j < inputArr[i].length; j++) {
            let jVal = inputArr[i][j]
            if(jVal !== '.') {
                let ret = []
                for(let k=-1;k<=1;k++)
                    for(let l=-1;l<=1;l++)
                    if((k||l) && i+k >= 0 && i+k < inputArr.length && j+l >= 0 && j+l < inputArr[0].length) 
                        ret.push(inputArr[(i+k)][(j+l)]);
                let totalCount = (ret.reduce((a, e) => { a[e] = a[e] ? a[e] + 1 : 1; return a }, {})); 
                let hashCount = (totalCount['#'] != undefined) ? totalCount['#'] : 0
                switch (jVal) {
                    case '#':
                        if(hashCount >= 4) {
                            tempArr[i][j] = 'L';
                            flagDirty = true;
                        }
                        break;
                    case 'L':
                        if(hashCount === 0) {
                            tempArr[i][j] = '#'
                            flagDirty = true
                        }
                        break;
                }
            }
        };
    };

    return {jsArray: JSON.stringify(tempArr), isDirty: flagDirty}
}

function countSurrounding(x :number, y: number, arrString : string):any {
    let inputArr = JSON.parse(arrString)
    let ret = []
    for(let i=-1;i<=1;i++)
        for(let j=-1;j<=1;j++)
        if((i||j) && x+i >= 0 && x+i < inputArr.length && y+j >= 0 && y+j < inputArr[0].length) 
            ret.push(inputArr[(x+i)][(y+j)]);

    let totalCount = (ret.reduce((a, e) => { a[e] = a[e] ? a[e] + 1 : 1; return a }, {})); 
    
    return {
        hashCount:(totalCount['#'] != undefined) ? totalCount['#'] : 0, 
        lCount:(totalCount['L'] != undefined) ? totalCount['L'] : 0, 
    }
}
// let len = input2D[0].length - 1
// console.log(countSurrounding(input2D.length - 1, len, JSON.stringify(input2D)))
let continueToApply = true
while(continueToApply) {
    let {isDirty, jsArray} = applyRules(JSON.stringify(input2D));
    continueToApply = isDirty;
    input2D = JSON.parse(jsArray);
}
let answer:number = 0
input2D.forEach(iVal => {
    iVal.forEach(element => {
        if(element === '#') answer++
    });
});




console.log(answer)