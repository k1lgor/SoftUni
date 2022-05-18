function ops(param1, param2, param3) {
	switch (param3) {
		case '+':
			console.log(param1 + param2);
			break;
		case '-':
			console.log(param1 - param2);
			break;
		case '*':
			console.log(param1 * param2);
			break;
		case '/':
			console.log(param1 / param2);
			break;
		case '%':
			console.log(param1 % param2);
			break;
		default:
			console.log(param1 ** param2);
			break;
	}
}
ops(5, 6, '+');
ops(3, 5.5, '*');
