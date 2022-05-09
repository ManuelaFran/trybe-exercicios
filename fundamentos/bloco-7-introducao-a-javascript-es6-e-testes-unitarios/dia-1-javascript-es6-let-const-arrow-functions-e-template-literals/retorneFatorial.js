const retorneFatorial = n => (n <= 0) ? 1: n * retorneFatorial(n-1);

console.log(retorneFatorial(4));