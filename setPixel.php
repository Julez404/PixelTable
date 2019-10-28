<?php

$row = $_GET['row'];
$column = $_GET['column'];
$color = $_GET['color'];

exec("./python/setPixel.py $row $column $color",$output);
print_r($output);

?>
