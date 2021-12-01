const {input} = require('./input');

function sum(array){
	return array.reduce((prev, curr) => prev + curr, 0);
}

let increaseCount = 0;

for (let index = 0; index < input.length; index++) {
	const a = sum(input.slice(index, index+3));
	const b = sum(input.slice(index+1, index+4));

	if(a < b){
		increaseCount++
	}
}

console.log('count: ', increaseCount);
