let inputString = "1X";
let size = inputString.length;

function addToString(str, inp) {

    if(str.length === size) {
        console.log('str ==== ', str);
        return;
    }
    
    let char = inp.shift()

    if(char === 'X') {
        addToString(str + '1', [...inp])
        addToString(str + '0', [...inp])
    } else {
        addToString(str + char, [...inp])
    }
}

addToString('', inputString.split(''))