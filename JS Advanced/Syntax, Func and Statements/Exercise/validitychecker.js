function checker(x1, y1, x2, y2) {
	const distance = (x1, y1, x2, y2) => {
		let dist = Math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2);
		let strValidator = Number.isInteger(dist) ? 'valid' : 'invalid';
		return `{${x1}, ${y1}} to {${x2}, ${y2}} is ${strValidator}`;
	};

	return `${distance(x1, y1, 0, 0)}\n${distance(x2, y2, 0, 0)}\n${distance(
		x1,
		y1,
		x2,
		y2
	)}`;
}
console.log(checker(3, 0, 0, 4));
console.log(checker(2, 1, 1, 1));
