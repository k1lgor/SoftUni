function largestNum(param1, param2, param3) {
	let arr = new Array(param1, param2, param3);
	console.log(`The largest number is ${Math.max(...arr)}.`);
}
largestNum(5, -3, 16);
largestNum(-3, -5, -22.5);
