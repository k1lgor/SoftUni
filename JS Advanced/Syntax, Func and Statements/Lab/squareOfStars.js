function square(param) {
	let result = '';
	for (let i = 0; i < param; i++) {
		for (let j = 0; j < param; j++) {
			result += '*' + ' ';
		}
		result += '\n';
	}
	console.log(result);
}
square(1);
square(2);
square(5);
square(7);
