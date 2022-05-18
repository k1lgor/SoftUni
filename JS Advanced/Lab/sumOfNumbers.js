function sum(param1, param2) {
	let result = 0;
	for (let i = Number(param1); i <= Number(param2); i++) {
		result += i;
	}
	console.log(result);
}
sum('1', '5');
sum('-8', 20);
