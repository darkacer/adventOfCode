const userInput = require('./data').getData()
const getNumAndName = require('./data').getNumAndName()
let dataMap = new Map();

// creates a map of parent to child with quantity
function sanitizeInput(string) {
    let thisbagName = string.split(' = ')[0].split(' bags')[0]
    let thisbagContains = string.split(' = ')[1]
    let array = []
    if(thisbagContains.includes(',')) {
        array = thisbagContains.split(', ').map(el => getNumAndName(el))
    }
    else if(!thisbagContains.includes('no')) {
        array.push(getNumAndName(thisbagContains))
    }
    dataMap.set(thisbagName, array)
}

function reccurse(string) {
    let count = 0;
    if(dataMap.get(string).length === 0) return 1

    dataMap.get(string).forEach(el => {
        count += el.quant * reccurse(el.name)
    })
    return count + 1
}

function main() {
    userInput.forEach(el => sanitizeInput(el))
    answer =  reccurse('shiny gold') - 1
    console.log('ans ', answer)
}

main()
// console.log('ans', dataMap)

