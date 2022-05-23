function sums(arr) {
	function inner(x, y) {
		return Number(x) + Number(y);
	}
	return inner(arr[0], arr[arr.length - 1]);
}
console.log(sums(['20', '30', '40']));
console.log(sums(['5', '10']));
