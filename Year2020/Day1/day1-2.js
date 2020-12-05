const user = require('./data');
let userInput = user.getData()

let total = 2020

const complementToX = (x,y) =>  x - y

function calc(w) {
	let sum = total - w;
	let num = 0
	let userInputSet = new Set(userInput)
	
	for(x of userInputSet) {
		if(w != x && complementToX(sum, x) !== w && userInputSet.has(complementToX(sum, x))) {
			num = x;
			break;
		}
	}
	return num
}

function main() {
	for(t of userInput) {
		num = calc(t)
		if(num) {
			console.log('first =', t, 'second =', num, 'third = ', total - t - num) 
			break;
		}
	}
}

main()