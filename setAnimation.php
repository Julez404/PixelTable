<?php

$animation = $_GET['animation'];
$color1 = $_GET['color1'];
$color2 = $_GET['color2'];
$text = $_GET['text'];
$speed = $_GET['speed'];

exec("./python/interface_setAnimation.py $animation $color1 $color2 $text $speed",$output);
print_r($output);

?>
