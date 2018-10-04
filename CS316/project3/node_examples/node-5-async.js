console.log('Hi');

setTimeout(function cb() {
	console.log('there');
	},
	0); // waits zero milliseconds

console.log('CS316 class');

// aysnchronous: prints:
// Hi
// CS316 class
// there
