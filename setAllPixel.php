<?php

$color = $_GET['color'];

exec("./python/interface_setAllPixel.py $color",$output);
print_r($output);

?>
