const userInput = require('./data').getData()

function getCommonFromSets(setA, setB) {
    setA.forEach(el => {
        if(!setB.has(el)) setA.delete(el)
    })
    return setA
}

function countCommonYesAnswers(stringList) {
    if(!stringList.length) return 0;
    // first 
    let baseAnswers = new Set(stringList[0]);
    // rest of the strings
    stringList.forEach(element => {
        baseAnswers = getCommonFromSets(baseAnswers, new Set(element))
    });
    return baseAnswers.size
}

const reducer = (acc, elem) => acc + countCommonYesAnswers(elem);

function main() {
    console.log('answer = ', userInput.reduce(reducer, 0))
}
main()