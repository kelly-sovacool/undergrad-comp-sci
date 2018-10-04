#!/usr/bin/ruby

def printFileContents(someFile)
	file = open(someFile)
	theContents = file.read
	puts theContents
end

printFileContents("shops.json")
