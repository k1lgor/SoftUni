function GCD(param1, param2) {
	// while (param2 != 0) {
	// 	if (param1 > param2) {
	// 		param1 -= param2;
	// 	} else {
	// 		param2 -= param1;
	// 	}
	// }
	// return param1;
	if (!param2) {
		return param1;
	}
	return GCD(param2, param1 % param2);
}
console.log(GCD(15, 5));
console.log(GCD(2154, 458));
