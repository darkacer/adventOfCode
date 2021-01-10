import { data } from "./data.ts"; 
function findMinAndMax(arr:number[]) :any {
    console.log(arr);
    
    let min = arr[0]
    let max = arr[0]

    arr.forEach(x => {
        if(min > x) min = x;
        if(max < x) max = x;
    })
    console.log(min, max)
    return min + max
}

// returns indexes in array where sum is equal to given number
function findSumAsNum(numArray:number[], sum:number) : any {
    let start = 0;
    let end = 0;

    let lastIndex = numArray.length - 1
    let currSum = numArray[0];

    while(start <= lastIndex && end <= lastIndex) {
        // console.log(start, end, currSum);
        
        if(currSum < sum) {
            end++;
            currSum += numArray[end]
        }
        else if(currSum > sum) {
            currSum -= numArray[start]
            start++;
        }
        else {
            break;
        }
    }
    return {start: start, end: end}
}

let inputArray = new data().returnData()
// let inputArray = [1,2,3,4,5];

let {start, end} = findSumAsNum(inputArray, 1504371145);
console.log('answer ', findMinAndMax(inputArray.slice(start, end+1)))