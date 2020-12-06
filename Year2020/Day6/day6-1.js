const userInput = require('./data').getData()

function countUniqueCharsInList(stringList) {
    let uniqueSet = new Set()
    stringList.forEach(string => {
        for(char of string) {
            uniqueSet.add(char)
        }
    });
    return uniqueSet.size
}

const reducer = (acc, elem) => acc + countUniqueCharsInList(elem);

function main() {
    let answer = userInput.reduce(reducer, 0)
    console.log('answer => ', answer)
}

main()