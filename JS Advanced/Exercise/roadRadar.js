function func(speed, area) {
	let limit;
	let diff;
	switch (area) {
		case 'motorway':
			limit = 130;
			break;
		case 'interstate':
			limit = 90;
			break;
		case 'city':
			limit = 50;
			break;
		default:
			limit = 20;
			break;
	}
	diff = Math.abs(speed - limit);
	if (speed <= limit) {
		return `Driving ${speed} km/h in a ${limit} zone`;
	} else {
		if (diff <= 20) {
			return `The speed is ${Math.abs(
				speed - limit
			)} km/h faster than the allowed speed of ${limit} - speeding`;
		} else if (20 < diff && diff <= 40) {
			return `The speed is ${Math.abs(
				speed - limit
			)} km/h faster than the allowed speed of ${limit} - excessive speeding`;
		} else {
			return `The speed is ${Math.abs(
				speed - limit
			)} km/h faster than the allowed speed of ${limit} - reckless driving`;
		}
	}
}
console.log(func(40, 'city'));
console.log(func(21, 'residential'));
console.log(func(120, 'interstate'));
console.log(func(200, 'motorway'));
