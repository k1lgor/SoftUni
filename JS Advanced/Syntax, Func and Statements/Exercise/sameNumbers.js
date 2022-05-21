function same(param) {
	const string = String(param);
	let total = 0;
	let isSame = false;
	for (let i = 0; i < string.length; i++) {
		total += Number(string[i]);
		for (let j = 0; j < string.length; j++) {
			if (i === j) {
				continue;
			} else if (string[i] === string[j]) {
				isSame = true;
			} else {
				isSame = false;
			}
		}
	}
	return `${isSame}\n${total}`;
}
console.log(same(2222222));
console.log(same(1234));
