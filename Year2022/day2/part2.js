import fs from "fs";
const scoreMap = {
    'r': 1,
    'p': 2,
    's': 3
}

const winLoseScore = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

const rpsMap = {
    'A': {'X': 'p', 'Y': 'r', 'Z': 's'},
    'B': {'X': 's', 'Y': 'p', 'Z': 'r'},
    'C': {'X': 'r', 'Y': 's', 'Z': 'p'}
}

function calculateScore(input1, result) {
    console.log(input1, result)
    let score = winLoseScore[result];
    
    console.log('first', score)

    console.log(rpsMap[input1])
    console.log(rpsMap[input1][result])
    score += scoreMap[rpsMap[input1][result]];
    console.log('second', score)
    return score
}


function main(inputArray) {
  let finalScore = inputArray.reduce((a,c) => a + calculateScore(c.split(' ')[0], c.split(' ')[1]), 0);
  console.log(finalScore);
}

fs.readFile("Year2022/day2/mydata.txt", "utf8", function (err, data) {
  if (err) throw err;
  main(data.split(/\r?\n/));
});
