<?php

$animation = $_GET['animation'];

exec("./python/setAnimation.py $animation",$output);
print_r($output);

?>
