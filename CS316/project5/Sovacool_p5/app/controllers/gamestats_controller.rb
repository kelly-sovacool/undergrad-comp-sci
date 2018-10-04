class GamestatsController < ApplicationController
  require "json"
  sports_file = open("public/Sports.json")
  sports_json = JSON.parse(sports_file.read)
  $titles = Array.new
  $results_options = Array.new
  $search_terms = Array.new
  $results_filenames = {}
  $filenames_to_sports = {}
  sports_json["sport"].each do |dict|
    $titles << dict["title"]
    $search_terms << dict["searchterms"]
    dict["results"].each do |key, value|
      $results_options << key
      $results_filenames[key] = value
	  $filenames_to_sports[value] = dict["title"]
    end
  end
  $search_terms.uniq!

  def search
    @thetitle = "FanXelk Search"
    @titles = $titles
    @results_options = $results_filenames
    @search_terms = $search_terms
  end

  def index
     @thetitle = "FanXelk"
  end

  def create
	@thetitle = "FanXelk Report"
  end
end
