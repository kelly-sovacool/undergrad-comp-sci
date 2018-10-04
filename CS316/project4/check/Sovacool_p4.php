<?php
/* 
Author: Kelly Sovacool
Date: 20 Nov. 2017
CS316-001
Project 4 - PHP
Implementation:
    a) Implemented
    b) Implemented
    c) Implemented
    d) Implemented
    e) Implemented
    f) Implemented
    g) Implemented
    h) Implemented
    i) Implemented
       Added "filter" option for coloring max or min searchterms.
       Wins are "greater" than losses.
       Selecting "all" has the same effect as not selecting anything for the filter (which does nothing).
Notes:
    Instead of having a showResults() function, I broke that up into multiple functions.
    The win/loss summary is output before all the game results, 'cause no one wants to scroll
        through a hundred or more games before getting to the summary.
    I don't know anything about sports. Really. But I have seen the movie "Space Jam". It's a classic.
*/

function parse_sports() {
    $filename = 'Sports.json';
    if (!file_exists($filename)) {
        echo "Error: Sports database is missing";
        return 500;
    }
    $string = file_get_contents($filename);
    $sports = json_decode($string, true);
    return $sports;
}

function get_options($sports) {
    $options = array();
    foreach ($sports['sport'] as $key1 => $value1) {
        foreach ($value1 as $key2 => $value2) {
            if (!array_key_exists($key2, $options)) {
                $options[$key2] = array();
            }
            if (is_array($value2)) {
                foreach ($value2 as $key3 => $value3) {
                    if (($key2 == "results") and (!in_array($key3, $options[$key2]))) {
                        $options[$key2][] = $key3;
                    }
                    else if ((($key2 == "searchterms") or ($key2 == "filter")) and !in_array($value3, $options[$key2])) {
                        $options[$key2][] = $value3;
                    }
                }
            }
            else if (!in_array($value2, $options[$key2])) {
                $options[$key2][] = $value2;
            }
        }
    }
    return $options;
}

function process_form($sports) {
	$form_options = array('title', 'results', 'searchterms', 'filter');
	$form_complete = true;
	foreach ($form_options as $index => $opt) {
        if (!array_key_exists($opt, $_GET)) {
            echo "<p>Error: $opt in HTML form not selected before submission.</p>";
            $form_complete = false;
        }
    }
	if ($form_complete) {
		$title = $_GET['title'];  
		$result = $_GET['results'];
		$search_term = $_GET['searchterms'];
		$filter = $_GET['filter'];
		$sport_title_found = false;
		foreach ($sports['sport'] as $key1 => $sport) {
			if ((array_key_exists('title', $sport)) and ($sport['title'] == $title)) {
				$sport_title_found = true;
				if (array_key_exists('results', $sport)) {
					foreach ($sport['results'] as $year => $file) {
					}
					if (array_key_exists($result, $sport['results'])) {
						$filename = $sport['results'][$result];
						if (file_exists($filename)) {
							$json = json_decode(file_get_contents($filename), true);
							print_results($title, $json, $search_term, $filter);
						}
						else {
							echo "<p>Error: results $result file not found</p>";
						}
					}
					else {
						echo "<p>Error: $result not in $title results</p>";
					}
				}
				else {
					echo "<p>Error: results $result not in $title database</p>";
				}
				break;
			}
		}
    
		if (!$sport_title_found) {
			echo "Error: sport $title not in database\n";
		}
	}
}

function start_html($title) {
    echo "<html>\n<head>\n<title>$title</title>\n<style type='text/css'></style>\n</head>\n<body>\n";
}

function end_html() {
    echo "\n</body>\n</html>\n";
}

function display_form($options) {

    start_html("fanXelk");
    echo "\n\t<form action='Sovacool_p4.php' method='get'>\n";
    foreach ($options as $form => $array) {
        echo "\t$form\n\t<select name='$form'>\n\t\t<option value=''>Select...</option>\n";
        if (is_array($array)) {
            foreach ($options[$form] as $key => $value) {
                echo "\t\t<option value='$value'>$value</option>\n";
            }
        }
		echo "\t</select>\n\n";
    }
    echo "\t<input type='submit' value='Search'>\n";
    echo "\t</form>\n";
    end_html();
}


function print_results($title, $result_json, $search_term, $filter) {
    if (json_last_error()) {
        echo json_last_error_msg();
    }
    else {
        $max_or_min = null;
        $wins = 0;
        $losses = 0;
        $style = "";
        $color = 'black';
        if (array_key_exists('comments', $result_json) and array_key_exists('games', $result_json)) {
            foreach ($result_json['games'] as $key => $game) {
				foreach ($game as $stat => $value) {
					if ($stat == "WinorLose") { // count wins & losses
						if ($value == "W") {
							$wins++;
						} 
						else if ($value == "L") {
							$losses++;
						}
					}
				}
				if (($filter == 'max') or ($filter == 'min')) { // find max/min
                    $value = $game[$search_term]; // determine max/min value
                    if (!$max_or_min or (($filter == 'max') and ($value > $max_or_min)) or (($filter == 'min') and ($value < $max_or_min))) {
                        $max_or_min = $value;
					}
				}
			}
			if ($filter == 'max') {
				$color = 'blue';
			}
			else if ($filter == 'min') {
				$color = 'red';
			}
            start_html($title);
            foreach ($result_json['comments'] as $key => $value) {
                echo "\t<h1>$value</h1>\n";
            }
            $win_percentage = 100 * $wins / ($wins + $losses);
            echo "\t<h4>Wins: $wins</h4>\n\t<h4>Losses: $losses</h4>\n\t<h4>Win Percentage: $win_percentage%</h4>\n\t<h2>Games:</h2>\n";
            $id_count = 0;
            foreach ($result_json['games'] as $key => $game) {
                foreach ($game as $stat => $value) {
					$id_count++;
                    if ($stat == $search_term) { // set font-style
						$h = 4;
						echo "\t<h$h style=\"font-style:bold;";
						if ($value == $max_or_min) { // set color
							echo "color:$color;";
						}
						else {
							echo "color:black;";
						}
					}
					else {
						$h = 6;
						echo "\t<h$h style=\"font-style:normal;color:black;";
					}
					if ($stat != "Opponent") {
						echo "text-indent:50px;";
					}
                    echo "\">$stat: $value</h$h>\n";
                }
			}
            end_html();
        }


        else {
            echo "Error: results file not formatted properly\n";
        }
    }
}
$sports = parse_sports();
if (json_last_error()) {
    echo json_last_error_msg();
}
else {
    $options = get_options($sports);
    if (json_last_error()) {
        echo json_last_error_msg();
    }
    else {
        if (isset($_GET['title']) and isset($_GET['results'])) {
            process_form($sports);
        } else {
            display_form($options);
        }
    }
}

?>
