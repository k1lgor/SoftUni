function func(year, month, day) {
	let prevDay = new Date(year, month, day).getDate() - 1;
	if (prevDay === 0) {
		month -= 1;
		prevDay = new Date(year, month, prevDay).getDate();
	}
	console.log(`${year}-${month}-${prevDay}`);
}
func(2016, 9, 30);
func(2016, 10, 1);
