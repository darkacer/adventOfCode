const userInput = require('./data').getData()
//const sanitizeInput = require('./data').sanitizeInput()

const sanitizeInput = (string) => {
    return {
        instruction: string.split(' ')[0],
        argument: parseInt(string.split(' ')[1].split(string.split(' ')[1][0])[1]),
        operator: string.split(' ')[1][0],
        dirty: false
    }
}

const add = (el) => (el.operator === '+') ? el.argument : el.argument * -1

function instructionReader(unputObjInsts) {
    let position = 0;
    let accumulator = 0;
    let count = 0
    while(true) {
        count++
        if(unputObjInsts[position].dirty) break;
        unputObjInsts[position].dirty = true;
        switch (unputObjInsts[position].instruction) {
            case 'acc':
                accumulator += add(unputObjInsts[position++])
                break;
            case 'jmp':
                position += add(unputObjInsts[position])
                break;
            case 'nop':
                position++
                break;
            default:
                break;
        }
    }
    console.log('position', position, 'count', count)
    return accumulator
}

function main() {
    console.log( instructionReader( userInput.map(el => sanitizeInput(el)) ) )
}

main()