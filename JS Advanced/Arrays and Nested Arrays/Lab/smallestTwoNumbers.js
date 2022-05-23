function small(arr) {
	return `${arr.sort((a, b) => a - b)[0]} ${arr.sort((a, b) => a - b)[1]}`;
}
console.log(small([30, 15, 50, 5]));
console.log(small([3, 0, 10, 4, 7, 3]));
