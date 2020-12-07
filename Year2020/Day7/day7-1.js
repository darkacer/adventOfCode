const userInput = require('./data').getData()
const getNumAndName = require('./data').getNumAndName()
let reverseMap = new Map();

// creates a map of child to parent without quantity
function findReverse(string) {
    thisbagName = string.split(' = ')[0].split(' bags')[0]
    thisbagContains = string.split(' = ')[1]
    let array = []
    if(thisbagContains.includes(',')) {
        array = thisbagContains.split(', ').map(el => getNumAndName(el).name)
    }
    else if(!thisbagContains.includes('no')) {
        array.push(getNumAndName(thisbagContains).name)
    }

    array.forEach(element => {
        if(reverseMap.has(element)) {
            reverseMap.get(element).push(thisbagName)
        } else {
            reverseMap.set(element, [thisbagName])
        }
    });
}

let countSet = new Set()

function reccurize(string) {
    if (!reverseMap.get(string)) return;
    reverseMap.get(string).forEach(el => {
        reccurize(el)
        countSet.add(el)
    })
    return
}

for(str in userInput) {
    findReverse(userInput[str])
}
reccurize('shiny gold')
console.log('final answe ', countSet.size)
