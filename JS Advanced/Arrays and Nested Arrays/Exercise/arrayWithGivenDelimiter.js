function solve(arr, deli) {
	return `${arr.join(deli)}`;
}
console.log(solve(['One', 'Two', 'Three', 'Four', 'Five'], '-'));
console.log(solve(['How about no?', 'I', 'will', 'not', 'do', 'it!'], '_'));
