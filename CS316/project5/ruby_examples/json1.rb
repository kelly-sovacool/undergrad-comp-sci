#!/usr/bin/ruby
#
require "json"

string =
'{"desc":{"someKey":"someValue","anotherKey":"value"},"main_item":{"stats":{"a":8,"b":12,"c":10}}}'
parsed = JSON.parse(string) # returns a hash

puts parsed["desc"]["someKey"]
puts parsed["main_item"]["stats"]["a"]

# Read JSON from a file, iterate over objects
file = open("shops.json")
json = file.read

parsed = JSON.parse(json)

parsed["shop"]["id"].each do |value|
  puts value
  end

