<?php

$row = $_GET['row'];
$column = $_GET['column'];
$color = $_GET['color'];

exec("./python/interface_setPixel.py $row $column $color",$output);
print_r($output);

?>
