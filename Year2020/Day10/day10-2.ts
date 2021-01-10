import { data } from "./data.ts"; 

let user = new data();

let inputArr = user.returnData().sort((a,b) => a-b)
inputArr.push(inputArr[inputArr.length - 1] + 3)
inputArr.unshift(0)

function createAdjecencyMap() {
	let adjecentMap:any = {}
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
}

let adjecentMap:any = createAdjecencyMap();

let source = inputArr[0]
let destination = inputArr[inputArr.length - 1]


let reachMap:any = {}

reachMap[destination] = 1

inputArr.reverse().forEach(el => {
    if(adjecentMap[el].length) {
        let mytotal = 0
        adjecentMap[el].forEach((em:number) => {
            if(reachMap.hasOwnProperty(em)) {
                mytotal += reachMap[em]
            }
        })
        reachMap[el] = mytotal
    }
})

console.log(reachMap[source]);