// Importing the fs module
import fs from 'fs'

function keepMaxN(arr, num, maxLen) {
    let arrLen = arr.length;
    let countPtr = arrLen - 1;
    arr.push(num)
    let numptr = arr.length - 1;
    while(countPtr >= 0 && numptr >= 0) {
        if(arr[countPtr] > arr[numptr]) break;
        else {
            // swap values on numptr and countptr
            let tempVal = arr[numptr];
            arr[numptr] = arr[countPtr];
            arr[countPtr] = tempVal;
            countPtr--;
            numptr--;
        }
    }
    console.log('arr ', arr)
    return arr.slice(0, maxLen)
}

function main(inputArray) {
  console.log(inputArray.length);
  let tempSum = 0;
  let finalMax = []
  inputArray.forEach(element => {
    if(element == '') { finalMax = keepMaxN(finalMax, parseInt(tempSum), 3); tempSum = 0 }
    else tempSum += parseInt(element);
  });
  console.log(finalMax)
  console.log(finalMax.reduce((a, c) => a + c, 0))
}



fs.readFile('Year2022/day1/my-file.txt', 'utf8', function(err, data) {
  if (err) throw err;
  main(data.split(/\r?\n/))
});

// console.log(keepMaxN([6000, 4000],12000, 3))