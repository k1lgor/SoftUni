function diagonal(matrix) {
	let primary = [];
	let secondary = [];
	let size = matrix.length;

	for (let i = 0; i < size; i++) {
		primary.push(matrix[i][i]);
		secondary.push(matrix[i][size - 1 - i]);
	}
	return `${primary.reduce((a, b) => a + b)} ${secondary.reduce(
		(a, b) => a + b
	)}`;
}
console.log(
	diagonal([
		[20, 40],
		[10, 60],
	])
);
console.log(
	diagonal([
		[3, 5, 17],
		[-1, 7, 14],
		[1, -8, 89],
	])
);
