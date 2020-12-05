const userInput = require('./data').getData()
const mapping = {'F': '0','B': '1','L': '0','R': '1'}

function getBinaryString(string) {
    for(letter of string) {
        string = string.replace(letter, mapping[letter])
    }
    return string
}
function main() {
    let max = 0
    userInput.forEach(el => {
        num = parseInt(getBinaryString(el), 2)
        // num = parseInt(getBinaryString(el.substring(0, 7)), 2) * 8 + parseInt(getBinaryString(el.substring(7, 10)), 2)
        if(num > max) max = num
    })
    console.log('max', max)
}
main()