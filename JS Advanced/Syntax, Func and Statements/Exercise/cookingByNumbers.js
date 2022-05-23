function func(num, param1, param2, param3, param4, param5) {
	let arr = new Array(param1, param2, param3, param4, param5);
	num = Number(num);

	arr.forEach((element) => {
		switch (element) {
			case 'chop':
				num /= 2;
				break;
			case 'dice':
				num = Math.sqrt(num);
				break;
			case 'spice':
				num++;
				break;
			case 'bake':
				num *= 3;
				break;
			default:
				num -= num * 0.2;
				break;
		}
		console.log(num);
	});
}
func('32', 'chop', 'chop', 'chop', 'chop', 'chop');
func('9', 'dice', 'spice', 'chop', 'bake', 'fillet');
