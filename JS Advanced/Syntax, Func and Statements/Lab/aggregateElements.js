// function ele(arr) {
// 	let sumOfArr = arr.reduce((a, b) => a + b);
// 	let inverse = arr.reduce((a, b) => a + 1 / b);
// 	let concat = [...arr].join('');
// 	console.log(sumOfArr);
// 	console.log(inverse);
// 	console.log(concat);
// }
// ele([1, 2, 3]);
// ele([2, 4, 8, 16]);
function ele(arr) {
	aggregate(arr, 0, (a, b) => a + b);
	aggregate(arr, 0, (a, b) => a + 1 / b);
	aggregate(arr, '', (a, b) => a + b);

	function aggregate(arr, initVal, func) {
		let val = initVal;
		for (let i = 0; i < arr.length; i++) {
			val = func(val, arr[i]);
		}
		console.log(val);
	}
}

ele([1, 2, 3]);
ele([2, 4, 8, 16]);
