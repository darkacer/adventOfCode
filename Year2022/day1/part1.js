// Importing the fs module
import fs from 'fs'

function main(inputArray) {
  console.log(inputArray.length);
  let tempSum = 0;
  let finalMax = 0
  inputArray.forEach(element => {
    if(element == '') { finalMax = tempSum > finalMax ? tempSum : finalMax; tempSum = 0}
    else tempSum += parseInt(element);
  });
  console.log(finalMax)
}



fs.readFile('Year2022/day1/my-file.txt', 'utf8', function(err, data) {
  if (err) throw err;
  main(data.split(/\r?\n/))
});