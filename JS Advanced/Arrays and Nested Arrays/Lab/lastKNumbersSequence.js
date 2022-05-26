function lastK(totalLength, lastNumbers) {
	let arr = [1];
	for (let i = 0; i < totalLength - 1; i++) {
		arr.push(arr.slice(-lastNumbers).reduce((a, b) => a + b));
	}
	return arr;
}
console.log(lastK(6, 3));
console.log(lastK(8, 2));
