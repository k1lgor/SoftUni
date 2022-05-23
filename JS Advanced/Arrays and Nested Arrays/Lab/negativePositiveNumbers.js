function sorting(arr) {
	let newArr = [];
	arr.forEach((element) => {
		if (element >= 0) {
			newArr.push(element);
		} else {
			newArr.unshift(element);
		}
	});
	return newArr.join('\n');
}
console.log(sorting([7, -2, 8, 9]));
console.log(sorting([3, -2, 0, -1]));
