// https://nodejs.org/api/http.html
//
// This example uses a named function doprocess() for the callback function
// sent to the createServer() method.

var http = require("http"),
	url = require('url');

const hostname = 'belgarath.cs.uky.edu';
const port = 3332;

function doprocess(request, response) {
	var xurl = request.url;
	response.statusCode = 200;
	response.setHeader('Content-Type', 'text/plain');
	response.end('Hello, World!  You requested the following URL: '+xurl+'\n');
}

var server = http.createServer(doprocess);
server.listen(port,hostname);












