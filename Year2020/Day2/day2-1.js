const user = require('./data');
let userInput = user.getData()


function main() {
    let answer = userInput.map(el => {
        return {
            mainString: el.split(' ')[2],
            letter: el.split(' ')[1][0],
            lowerLim: el.split(' ')[0].split('-')[0],
            upperLim: el.split(' ')[0].split('-')[1]
        }
    }).filter(el => {
        let numberOfletters = el.mainString.includes(el.letter) ? el.mainString.match(new RegExp(el.letter, 'g')).length : 0;
        return (numberOfletters >= el.lowerLim && numberOfletters <= el.upperLim)
    }).length

    console.log(answer)
}
main()