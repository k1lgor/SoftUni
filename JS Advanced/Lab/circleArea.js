function area(param) {
	if (typeof param === 'number') {
		console.log(`${(Math.PI * Math.pow(param, 2)).toFixed(2)}`);
	} else {
		console.log(
			`We can not calculate the circle area, because we receive a ${typeof param}.`
		);
	}
}
area(5);
area('name');
