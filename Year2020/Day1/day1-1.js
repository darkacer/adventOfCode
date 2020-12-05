const user = require('./data');
let userInput = user.getData()


const complementToX = (x,y) =>  x - y

function main() {
	let userInputSet = new Set(userInput)
	let num;
	for(x of userInput) {
		console.log('x=>',x);
		if (userInputSet.has(complementToX(2020, x))) {
			num = x;
			break
		}
	}
	console.log(num)
	console.log('answer', num * (2020 - num))
}

main()