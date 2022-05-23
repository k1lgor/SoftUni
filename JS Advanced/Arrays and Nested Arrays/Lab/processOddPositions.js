function func(arr) {
	let newArr = [];
	for (let i = 0; i < arr.length; i++) {
		if (i % 2 !== 0) {
			newArr.push(arr[i] * 2);
		}
  }
  return newArr.reverse().join(' ')
}
console.log(func([10, 15, 20, 25]));
console.log(func([3, 0, 10, 4, 7, 3]));
