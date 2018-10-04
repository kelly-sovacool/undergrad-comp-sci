<?php

require("php-html.php");
require("php-menus.php");
require("php-database.php");

do_html_start();

do_menu();

echo "<p><p>";

someLookup();

do_html_end();
?>
