const user = require('./data');
let userInput = user.getData()

function main() {
    let answer = userInput.map(el => {
        return {
            mainString: el.split(' ')[2],
            letter: el.split(' ')[1][0],
            validPosition: el.split(' ')[0].split('-')[0] - 1,
            inValidPosition: el.split(' ')[0].split('-')[1] - 1
        }
    }).filter(el => {
        return (el.mainString[el.validPosition] === el.letter) !== (el.mainString[el.inValidPosition] === el.letter)
    }).length

    console.log(answer)
}
main()