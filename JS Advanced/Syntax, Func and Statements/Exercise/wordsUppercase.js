function upper(str) {
	let regex = /[a-zA-Z0-9]+/g;
	let arr = str.match(regex);
	let newArr = [];
	arr.forEach((element) => {
		newArr.push(element.toUpperCase());
	});
	return newArr.join(', ');
}
console.log(upper('Hi, how are you?'));
console.log(upper('hello'));
