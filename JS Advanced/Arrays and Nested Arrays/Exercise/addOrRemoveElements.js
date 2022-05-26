function solve(arr) {
	let initial = 0;
	let newArr = [];
	arr.filter((a) => {
		if (a === 'add') {
			newArr.push(++initial);
		} else if (a === 'remove' && newArr !== []) {
			initial++;
			newArr.pop();
		}
	});
	return newArr.length !== 0 ? newArr.join('\n') : 'Empty';
}
console.log(solve(['add', 'add', 'add', 'add']));
console.log(solve(['add', 'add', 'remove', 'add', 'add']));
console.log(solve(['remove', 'remove', 'remove']));
