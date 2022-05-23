function piece(arr, start, end) {
	return arr.slice(arr.indexOf(start), arr.indexOf(end) + 1);
}
console.log(
	piece(
		[
			'Pumpkin Pie',
			'Key Lime Pie',
			'Cherry Pie',
			'Lemon Meringue Pie',
			'Sugar Cream Pie',
		],
		'Key Lime Pie',
		'Lemon Meringue Pie'
	)
);
console.log(
	piece(
		[
			'Apple Crisp',
			'Mississippi Mud Pie',
			'Pot Pie',
			'Steak and Cheese Pie',
			'Butter Chicken Pie',
			'Smoked Fish Pie',
		],
		'Pot Pie',
		'Smoked Fish Pie'
	)
);
