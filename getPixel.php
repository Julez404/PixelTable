<?php

$row = $_GET['row'];
$column = $_GET['column'];

exec("./python/getPixel.py $row $column",$output);
print_r($output);

?>
