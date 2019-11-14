<?php

$color = $_GET['color'];
$hours = $_GET['hours'];
$minutes = $_GET['minutes'];
$seconds= $_GET['seconds'];

exec("./python/interface_setTimer.py $color $hours $minutes $seconds",$output);
print_r($output);

?>
