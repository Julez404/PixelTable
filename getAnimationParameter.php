<?php

$animation = $_GET['animation'];

exec("./python/getAnimationParameter.py $animation",$output);
print_r($output);

?>
