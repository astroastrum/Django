console.log('블루베리' == '블루베리'); // true
console.log(1000 < 6000); // true
console.log(1000 > 6000); // false

const array1 = [6, 7, 8];
const array2 = [6, 7, 8];
console.log(array1 == array2); // 참조하는 array가 달라서 false

const array6 = [6, 7, 8];
const array7 = array6;
console.log(array6 == array7); // 참조하는 array가 동일해서 true
