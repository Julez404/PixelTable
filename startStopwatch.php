<?php

$color = $_GET['color'];

exec("./python/setStopwatch.py $color",$output);
print_r($output);

?>
