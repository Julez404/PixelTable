<?php

$color = $_GET['color'];

exec("./python/startStopwatch.py $color",$output);
print_r($output);

?>
