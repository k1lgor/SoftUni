function length(param1, param2, param3) {
	let arr = new Array(param1, param2, param3);
	let sumOfArr = 0;
	arr.forEach((element) => {
		sumOfArr += element.length;
	});
	console.log(`${sumOfArr}\n${Math.floor(sumOfArr / arr.length)}`);
}
length('chocolate', 'ice cream', 'cake');
length('pasta', '5', '22.3');
