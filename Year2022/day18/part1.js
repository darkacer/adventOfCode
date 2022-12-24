import fs from "fs";

let inpArry = [];
let plotArray = [];

let xMax = 0
let yMax = 0
let zMax = 0




function main(inputArray) {
//   console.log(inputArray);
  inputArray.forEach((el) => inpArry.push(el.split(",")));
  console.log("total array ", inpArry);
  findMaxs(inpArry);

  findTotalNieghbours();

//   console.log(plotArray);
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

    console.log('plotarray -- ' + JSON.stringify(plotArray))

}

function findTotalNieghbours() {
    let totalNeighbours = 0;
    inpArry.forEach(el => {
        totalNeighbours += howManyNeighboursFor(el[0],el[1],el[2]);
    })

    console.log('totalNeighbours', totalNeighbours)
    console.log('total sides ', inpArry.length * 6)

    console.log('finalAnswer' , inpArry.length * 6 - totalNeighbours)
}

function howManyNeighboursFor(x,y,z) {
    let neighbours = 0
    if(x - 1 >= 0 && plotArray[x - 1][y][z] == 1) neighbours++; 
    if(y - 1 >= 0 && plotArray[x][y - 1][z] == 1) neighbours++; 
    if(z - 1 >= 0 && plotArray[x][y][z - 1] == 1) neighbours++; 
    if(x + 1 < xMax && plotArray[x + 1][y][z] == 1) neighbours++; 
    if(y + 1 < yMax && plotArray[x][y + 1][z] == 1) neighbours++; 
    if(z + 1 < zMax && plotArray[x][y][z + 1] == 1) neighbours++; 

    return neighbours;
}


fs.readFile("Year2022/day18/data.txt", "utf8", function (err, data) {
  if (err) throw err;
  main(data.split(/\r?\n/));
});

