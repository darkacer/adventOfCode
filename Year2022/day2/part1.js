import fs from "fs";
const player1Mods = {
    'A': 'r',
    'B': 'p',
    'C': 's'
}
const player2Mods = {
    'X': 'r',
    'Y': 'p',
    'Z': 's'
}

const scoreMap = {
    'r': 1,
    'p': 2,
    's': 3
}
function winDeterminer(arr) {
    console.log('arr ', arr)
    let input1 = player1Mods[arr[0]]
    let input2 = player2Mods[arr[1]]

    const valueMap = {
        'r': 's',
        's': 'p',
        'p': 'r'
    }
    let score = scoreMap[input2];
    console.log('score', score)
    if(valueMap[input1] == input2) score += 0;
    else if(valueMap[input2] == input1) score += 6;
    else score += 3;

    console.log('score', score)
    return score;
}

function main(inputArray) {
  let finalScore = inputArray.reduce((a,c) => winDeterminer(c.split(' ')) + a, 0)
  console.log(finalScore)

}




fs.readFile("Year2022/day2/mydata.txt", "utf8", function (err, data) {
  if (err) throw err;
  main(data.split(/\r?\n/));
});
