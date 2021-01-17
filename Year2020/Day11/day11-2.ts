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
                let x, y = 0
                let ret = []

                // go left
                y = j
                while(--y >= 0){
                    let left = inputArr[i][y];
                    if(left !== '.')  {ret.push(left); break}
                }

                //go left-up
                x = i
                y = j
                while(--x >= 0 && --y >= 0) {
                    let topLeft = inputArr[x][y]
                    if(topLeft !== '.') {ret.push(topLeft); break}
                }

                // go top
                x = i
                while(--x >= 0) {
                    let top = inputArr[x][j]
                    if(top  !== '.') {ret.push(top); break}
                }

                // go top right
                x = i
                y = j
                while(--x >= 0 && ++y < inputArr[0].length) {
                    let topRight = inputArr[x][y]
                    if(topRight !== '.') {ret.push(topRight); break}
                }

                // go right
                y = j
                while(++y < inputArr[0].length) {
                    let right = inputArr[i][y]
                    if(right !== '.') {ret.push(right); break}
                }

                // bottom right
                x = i
                y = j
                while(++x < inputArr.length && ++y < inputArr[0].length) {
                    let bottomRight = inputArr[x][y]
                    if(bottomRight !== '.') {ret.push(bottomRight); break}
                }

                // bottom
                x = i
                while(++x < inputArr.length) {
                    let bottom = inputArr[x][j]
                    if(bottom !== '.') {ret.push(bottom); break}
                }

                // bottom left
                x = i
                y = j
                while(++x < inputArr.length && --y >= 0) {
                    let bottomLeft = inputArr[x][y]
                    if(bottomLeft !== '.') {ret.push(bottomLeft); break}
                }

                let totalCount = (ret.reduce((a, e) => { a[e] = a[e] ? a[e] + 1 : 1; return a }, {})); 
                let hashCount = (totalCount['#'] != undefined) ? totalCount['#'] : 0
                switch (jVal) {
                    case '#':
                        if(hashCount >= 5) {
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