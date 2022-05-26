function biggest(arr) {
	return `${Math.max(...arr.flat())}`;
}
console.log(
	biggest([
		[20, 50, 10],
		[8, 33, 145],
	])
);
console.log(
	biggest([
		[3, 5, 7, 12],
		[-1, 4, 33, 2],
		[8, 3, 0, 4],
	])
);
