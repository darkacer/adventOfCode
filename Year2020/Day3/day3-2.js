const user = require('./data');
let userInput = user.getData()
let jumpInput = user.getJumpInput()

function findNoOfTrees(userInput, xJump, yJump) {
    let x = 0;
    let y = 0;
    let noOfTrees = 0;
    let tree = '#'

    while(y < userInput.length) {
        el = userInput[y]
        if(el[x % el.length] === tree) noOfTrees++
        x += xJump
        y += yJump
    }
    return noOfTrees
}

function main() {
    console.log( jumpInput.reduce((a,el) => a * findNoOfTrees(userInput, el.x, el.y), 1) )
}
main()