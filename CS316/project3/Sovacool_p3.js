// Project 3 - Node.js & HTTP
// Author: Kelly Sovacool
// Date: 30 Oct. 2017

var http = require("http")
var url = require('url')
var fs = require('fs');

const start_port = 2000;
const end_port = 30000;
const hostname = 'penstemon.cs.uky.edu';
var server = http.createServer(serveURL);
var port = random_port();
server.listen(port, hostname, function() {
    console.log("Server started. Listing on http://"+hostname+":"+port);
});

function serveURL(request, response) { 
	// serve a requested file or advertisement (33% of the time)
	// give error message if path is invalid or file does not exist
    var xurl = request.url;
	var path = xurl.replace(/^\//, "");
	var is_valid_path = isValid(path);
	var file_exists = fs.existsSync(path);
    console.log('url: ' + xurl);
	console.log('path: ' + path);
	console.log('is valid path: ' + is_valid_path);
	console.log('file exists: ' + file_exists);
    if (is_valid_path && file_exists) {
		var should_advertise = randomly_advertise();
		console.log('advertise: ' + should_advertise);
		if (should_advertise) {
				path = 'advert.jpg';
		}
		giveFile(path, response);
	}
    else {
        giveErrorMessage(xurl, response);
    }
}

function isValid(path) { 
	// check if a file path is valid
    var is_valid;
	// must start with alphanumberic character and end in either .jpg or .mp3
	var regex = new RegExp("^[A-Za-z0-9_-]*.(jpg|mp3)");
    var match = regex.exec(path);
    if (match && (match[0] === path)) {
        is_valid = true;
    }
    else {
        is_valid = false;
    }
    return is_valid;
}

function giveErrorMessage(xurl, response) { 
	// give an error message
	console.log("Error: file is not valid or does not exist.");
    response.writeHead('403', {'Content-Type': 'text/plain'});
    response.end('The file you requested '+xurl+' is not valid or does not exist.\n');
}

function giveFile(path, response) { 
	// give a jpg or mp3 file
    var extension = path.slice(-3);
	var content_type;
	console.log('extension: '+extension);
    if (extension === 'mp3') {
		content_type = 'audio/mp3';
    }

    else if (extension === 'jpg') {
		content_type = 'image/jpg';
    }
    else {
        console.error("invalid extension "+extension+" made it past isValid()")
		response.writeHead('403', {'Content-Type': 'text/plain'});
		response.end('The file you requested '+path+' has an invalid extension '+extension+'.\n');
    }
	fs.readFile(path, function (error, data) {
		if (error) throw error;
		response.writeHead('200', {'Content-Type': content_type});
		response.end(data);
	});
}

function randomly_advertise() { 
	// choose whether to advertise or return requested file
    var advertise;
    if ((Math.random() * 100) <= 32) { advertise = true; }
    else { advertise = false;}
    return advertise;
}

function random_port() { 
	// pick a random port within the start and end ports
    return Math.floor(Math.random() * (end_port + 1 - start_port) + start_port);
}
