let inputString = "X1";
let size = inputString.length;

function addToString(str:string, inp:string[]): void {
    let tempInp = inp
    
    if(str.length === size || inp.length === 0) {
        console.log('str ==== ', str);
        return;
    }
    
    let char:any = tempInp.shift()
    if(char === 'X') {
        addToString(str + '1', [...tempInp])
        addToString(str + '0', [...tempInp])
    } else {
        addToString(str + char, [...tempInp])
    }
    return;
}

addToString('', inputString.split(''))