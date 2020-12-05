const user = require('./data');
let userInput = user.getData()
let requiredFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

function isValidInfo(record) {
    return requiredFields.every(em => record.includes(em))
}

function main() {
    let count = 0
    userInput.forEach(el => {
        if(isValidInfo(el)) count++
    })
    console.log('answer ', count)
}

main()