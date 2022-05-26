function biggest(arr) {
	return `${Math.max(...arr.flat())}`;
	// let big = -99999999999999999;
	// for (let i = 0; i < arr.length; i++) {
	// 	for (let j = 0; j < arr[i].length; j++) {
	// 		if (arr[i][j] > big) {
	// 			big = arr[i][j];
	// 		}
	// 	}
	// }
	// arr.filter((a) => {
	// 	for (const iterator of a) {
	// 		if (iterator > big) {
	// 			big = iterator;
	// 		}
	// 	}
	// });
	// return big;
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
