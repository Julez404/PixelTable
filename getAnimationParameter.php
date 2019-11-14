<?php

$animation = $_GET['animation'];

exec("./python/interface_getAnimationParameter.py $animation",$output);
print_r($output);

?>
