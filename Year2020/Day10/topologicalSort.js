import { data } from "./data.ts"; 

let user = new data();


let inputArr = user.returnData().sort((a,b) => a-b)
inputArr.push(inputArr[inputArr.length - 1] + 3)
inputArr.unshift(0)
console.log(inputArr);

let source = inputArr[0];
let destination = inputArr[inputArr.length - 1]
// let destination = 158
let count = 0
let adjecentMap = {}
function createAdjecencyMap() {
	for(let i = 0; i < inputArr.length; i++) {
		let curNum = inputArr[i];
		let tempArr = []
		for(let j = i + 1; j <= i + 3; j++) {
			if(inputArr[j] <= curNum + 3) {
				tempArr.push(inputArr[j])
			}
		}
		adjecentMap[curNum] = tempArr
	}
	return adjecentMap
	// return {
	// 	0: [1, 2, 3, 4],
	// 	2: [3],
	// 	3: [4],
	// }
}


function getNeibours(int) {
	return adjecentMap[int];
}

function getRoute(point) {
	// console.log('inscide', point, destination);
	
	if(point === destination) {
		count++
		console.log('count', count);
		
		return;
	}
	if(getNeibours(point)) {
		for(let i = 0; i < getNeibours(point).length; i++) {
			getRoute(getNeibours(point)[i])
		}
	} else {
		return;
	}
}


adjecentMap = createAdjecencyMap();
console.log('adjecentMap', adjecentMap)
getRoute(source);
console.log('count', count);
