<?php

$color = $_GET['color'];

exec("./python/interface_setStopwatch.py $color",$output);
print_r($output);

?>
