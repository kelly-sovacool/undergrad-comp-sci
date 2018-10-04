start_port = 2000;
end_port = 30000;
function random_port() {
	return Math.floor(Math.random() * (end_port + 1 - start_port) + start_port);
}
process.stdout.write("port: " + random_port());
