// run with call stack set to 5000
// since reccursion is used

import fs from "fs";

let inpArry = [];
let plotArray = [];

let xMax = 0
let yMax = 0
let zMax = 0

let deleteMECounter = 0;


function main(inputArray) {
//   console.log(inputArray);
  inputArray.forEach((el) => inpArry.push(el.split(",")));
  console.log("total array ", inpArry);
  findMaxs(inpArry);

  floodFillAlgo();

}


// a function that takes input and creates a 3d array 
// where if block present at (2,2,2) then plotArray[2][2][2] = 1 
// else plotArray[x][y][z] = 0
function findMaxs() {
    inpArry.forEach(el => {
        el[0] = parseInt(el[0])
        el[1] = parseInt(el[1])
        el[2] = parseInt(el[2])
        xMax = xMax < el[0] ? el[0] : xMax
        yMax = yMax < el[1] ? el[1] : yMax
        zMax = zMax < el[2] ? el[2] : zMax
    })

    console.log(xMax, yMax, zMax)
    xMax += 1
    yMax += 1
    zMax += 1

    plotArray = new Array(xMax).fill(0).map(() => new Array(yMax).fill(0).map(() => new Array(zMax).fill(0)));

    inpArry.forEach(el => {
        let x = el[0]
        let y = el[1]
        let z = el[2]
        plotArray[x][y][z] = 1
    })
}

function floodFillAlgo() {
    // make corners fill with Lava
    // 0 is no block
    // 1 is block
    // 2 is lava
    // start applying flood fill algo over from the corners
    

    // now reccursively find all the points at which the lava can flow 
    spreadLava([[0,0,0]])
    console.log('deleteMECounter', deleteMECounter)
    console.log(JSON.stringify (plotArray));
    countHowMaySidesFaceLava();
}

function spreadLava(currentHostsOfLava) {
    deleteMECounter++;
    if (currentHostsOfLava.length == 0) return;
    currentHostsOfLava.forEach(point => {
        let x = point[0]
        let y = point[1]
        let z = point[2]
        if(plotArray[x][y][z] != 1) plotArray[x][y][z] = 2;
        else return;
        let nextHosts = []
        if(x - 1 >= 0 && plotArray[x - 1][y][z] == 0) nextHosts.push([x - 1, y, z])
        if(y - 1 >= 0 && plotArray[x][y - 1][z] == 0) nextHosts.push([x, y - 1, z])
        if(z - 1 >= 0 && plotArray[x][y][z - 1] == 0) nextHosts.push([x, y, z - 1])
        if(x + 1 < xMax && plotArray[x + 1][y][z] == 0) nextHosts.push([x + 1, y, z])
        if(y + 1 < yMax && plotArray[x][y + 1][z] == 0) nextHosts.push([x, y + 1, z])
        if(z + 1 < zMax && plotArray[x][y][z + 1] == 0) nextHosts.push([x, y, z + 1])

        if(nextHosts.length > 0) spreadLava(nextHosts);
    })
}

function countHowMaySidesFaceLava() {
    console.log(JSON.stringify (plotArray));
    let finalAnswer = 0;
    inpArry.forEach(point => {
        let blockside =  howManyNeighboursFor(point[0], point[1], point[2])
        finalAnswer += blockside
    })
    console.log('final answer ' , inpArry.length * 6 - finalAnswer)
}

function howManyNeighboursFor(x,y,z) {
    let blockside = 0
    if(x - 1 >= 0 && plotArray[x - 1][y][z] != 2) blockside++; 
    if(y - 1 >= 0 && plotArray[x][y - 1][z] != 2) blockside++; 
    if(z - 1 >= 0 && plotArray[x][y][z - 1] != 2) blockside++; 
    if(x + 1 < xMax && plotArray[x + 1][y][z] != 2) blockside++; 
    if(y + 1 < yMax && plotArray[x][y + 1][z] != 2) blockside++; 
    if(z + 1 < zMax && plotArray[x][y][z + 1] != 2) blockside++;

    return blockside;
}


fs.readFile("Year2022/day18/data.txt", "utf8", function (err, data) {
  if (err) throw err;
  main(data.split(/\r?\n/));
});

