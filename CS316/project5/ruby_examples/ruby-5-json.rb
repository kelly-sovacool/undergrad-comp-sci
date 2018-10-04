#!/usr/bin/ruby

require "json"

def printFileContents(someFile)
	file = open(someFile)
	theContents = file.read
	printJSON(theContents)
end

def printJSON(someJSON)
	
	theShopStuff = JSON.parse(someJSON)

# there is only one "shop" element, so access its subelements directly:

	theShopStuff["shop"]["locations"].each do |aNumber,where|
		puts "Store id: #{aNumber} is in #{where}"
	end
	theShopStuff["shop"]["id"].each do |theID|
		puts "\t #{theID}"
	end
end


printFileContents("shops.json")
