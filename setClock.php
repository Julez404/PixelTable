<?php

$color = $_GET['color'];

exec("./python/setClock.py $color",$output);
print_r($output);

?>
