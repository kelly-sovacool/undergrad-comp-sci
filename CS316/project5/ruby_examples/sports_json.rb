#!/usr/bin/ruby
require "json"
sports_file = open("Sports.json")
sports_json = JSON.parse(sports_file.read)
titles = Array.new
results = Array.new
search_terms = Array.new
results_filenames = {}
sports_json["sport"].each do |dict|
  titles << dict["title"]
  search_terms << dict["searchterms"]
  dict["results"].each do |key, value|
    results << key
    results_filenames[key] = value
  end
search_terms.uniq!
end
puts "titles"
puts titles
puts "\nresults"
puts results
puts "\nsearch terms"
puts search_terms
puts "\nresults filenames"
puts results_filenames
