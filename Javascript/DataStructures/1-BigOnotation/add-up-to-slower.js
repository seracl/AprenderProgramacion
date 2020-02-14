function addUpTo(n) {
  let total = 0;
  for (let i = 1; i <= n; i++) {
    total += i;
  }
  return total;
}

var t1 = Date.now();
let result = addUpTo(10);
var t2 = Date.now();
console.log("Slow result: ", result);
console.log(`Time Elapsed: ${(t2 - t1) / 1000} seconds.`);