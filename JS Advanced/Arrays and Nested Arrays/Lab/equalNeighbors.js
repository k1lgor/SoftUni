function equal(matrix) {
	let repeat = 0;
	for (let row = 0; row < matrix.length; row++) {
		for (let col = 0; col < matrix[row].length - 1; col++) {
			if (matrix[row][col] === matrix[row][col + 1]) {
				repeat++;
			}
		}
	}
	let size = matrix[0].length;
	for (let col = 0; col < size; col++) {
		for (let row = 0; row < matrix.length - 1; row++) {
			if (matrix[row][col] === matrix[row + 1][col]) {
				repeat++;
			}
		}
	}
	return repeat;
}
console.log(
	equal([
		['2', '3', '4', '7', '0'],
		['4', '0', '5', '3', '4'],
		['2', '3', '5', '4', '2'],
		['9', '8', '7', '5', '4'],
	])
);
console.log(
	equal([
		['test', 'yes', 'yo', 'ho'],
		['well', 'done', 'yo', '6'],
		['not', 'done', 'yet', '5'],
	])
);
