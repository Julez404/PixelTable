<?php

$color = $_GET['color'];

exec("./python/setAllPixel.py $color",$output);
print_r($output);

?>
