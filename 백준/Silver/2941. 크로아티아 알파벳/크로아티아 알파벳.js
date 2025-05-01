const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();

const croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="];

let str = input;

for (let pattern of croatia) {
    str = str.split(pattern).join("!"); 
}

console.log(str.length);
