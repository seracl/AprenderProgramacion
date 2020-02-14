function addUpTo(n) {
	for (var i = 0; i < n; i++) {
		for (var j = 0; j < n; j++) {
			for (var k = 0; k < n; k++) {
				console.log(i, j, k);
			}
		}
	}
}
let t1 = +Date.now();
let result = addUpTo(5);
let t2 = +Date.now();
console.log("Test result: ", result);
console.log(`Time elapsed: ${(t2 - t1) / 1000} seconds.`);