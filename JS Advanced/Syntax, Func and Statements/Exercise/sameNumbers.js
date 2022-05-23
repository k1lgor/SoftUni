function same(param) {
	let arr = String(param).split('');
	let total = arr.reduce((a, b) => Number(a) + Number(b));
	let isSame = arr.every((a) => a === arr[0]) ? true : false;
	return `${isSame}\n${total}`;
}
console.log(same(2222222));
console.log(same(1234));
