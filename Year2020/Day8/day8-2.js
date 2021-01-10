const Node = require('./node.js')
const sanitizeInput = require('./data').sanitizeInput()
const userInput = require('./data').getData()

//console.log(firstNode.NextNode.NextNode.instruction)

const findNieghbors = (elem, i) => {
    // In acc's case we care about the natural next node only so just update those
    if(elem.instruction === 'acc') {
        elem.nextNode = i + 1;
        elem.psuedoNext = -1
    }
    if(elem.instruction === 'nop') {
        elem.nextNode = i + 1
        elem.psuedoNext = (elem.operator === '+') ? i + elem.argument : i - elem.argument
    }
    if(elem.instruction === 'jmp') {
        elem.psuedoNext = i + 1
        elem.nextNode = (elem.operator === '+') ? i + elem.argument : i - elem.argument
    }
}

objectList = userInput.map(el => new Node(sanitizeInput(el)))

objectList.push(new Node({instruction: 'end', operator:'', argument:0}))

for(let i = 0; i < objectList.length - 1; i++) {
    findNieghbors(objectList[i], i)
}

let nextNodeMap = new Map();
let psuedoNextMap = new Map();

for(let i = 0; i < objectList.length - 1; i++) {
    let pnext = objectList[i].psuedoNext
    let next = objectList[i].nextNode
    if(pnext !== -1) {
        if(!psuedoNextMap.has(pnext)) {
            psuedoNextMap.set(pnext, [i])
        } else {
            psuedoNextMap.set(pnext, [...psuedoNextMap.get(pnext), i])
        }
    }
    
    if(!nextNodeMap.has(next)) {
        nextNodeMap.set(next, [i])
    } else {
        nextNodeMap.set(next, [...nextNodeMap.get(next), i])
    }
    
}
let deadEnd = []

function findDeadEnd(x) {
    if(!nextNodeMap.has(x)){ 
        deadEnd.push(x) 
        return
    }
    nextNodeMap.get(x).forEach(el => findDeadEnd(el))
}

x = objectList.length - 1

findDeadEnd(x)

console.log('deadEnd targets', deadEnd)
let tobeChanged = []
deadEnd.forEach(el => {
    console.log(el, psuedoNextMap.get(el))
    tobeChanged.push(psuedoNextMap.get(el)[0])
    //reachNoOne(psuedoNextMap.get(el)[0])
})

console.log('tobeChanged', tobeChanged)
let i = 0;
while(true) {
    if(tobeChanged.includes(i)) break;
    i = objectList[i].nextNode
}
console.log('i', i)

// function reachNoOne(x) {
//     console.log('x is ', x)
//     while(nextNodeMap.has(x)) {
//         console.log('x is', x, nextNodeMap.get(x))
//         x = nextNodeMap.get(x)[0]
//     }
//     if(x === 1) console.log('reached !!!')
// }




// while(nextNodeMap.has(x)) {
//     console.log('x is', x)
//     console.log('full depth', nextNodeMap.get(x))
//     x = nextNodeMap.get(x)[0]
    
// }
// console.log('target is == ', x)
// console.log('i can reach the target', psuedoNextMap.get(x))




// console.log(objectList[0], objectList[1], objectList[2])
// console.log(objectList[0], objectList[1], objectList[2])