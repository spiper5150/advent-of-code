const {input} = require('./input');

let count = 0;

for (let index = 0; index < input.length; index++) {
	const a = input[index];
	const b = input[index+1];

	if(a < b){
		count++
	}
}

console.log('count: ', count);
