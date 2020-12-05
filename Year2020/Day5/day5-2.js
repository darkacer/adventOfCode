const userInput = require('./data').getData()
const mapping = {'F': '0','B': '1','L': '0','R': '1'}

function getBinaryString(string) {
    for(letter of string) {
        string = string.replace(letter, mapping[letter])
    }
    return parseInt(string, 2)
}

function main() {
    let max = getBinaryString(userInput[0])
    let min = getBinaryString(userInput[0])
    let sum = 0
    userInput.forEach(el => {
        num = getBinaryString(el)
        if(num < min) min = num
        if(num > max) max = num
        sum += num
    })
    let answer = (min + max) * (userInput.length + 1) / 2 - sum

    console.log(answer)
}

main()