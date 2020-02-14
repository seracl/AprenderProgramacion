//Linear Function
//Accept an array and a value
//Loop through the array and check if the current array element is equal to the value
//If it is, return the index at which the element is found
//Else, return -1

function linearSearch(arry, val) {
	for (var i = 0; i <= arry.length; i++) {
		if (arry[i] === val) {
			return i;
		}
	}
}

console.log(linearSearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 8));