<?php

$color = $_GET['color'];

exec("./python/interface_setClock.py $color",$output);
print_r($output);

?>
