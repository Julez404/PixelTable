<?php

$color = $_GET['color'];
$hours = $_GET['hours'];
$minutes = $_GET['minutes'];

exec("./python/interface_setAlarm.py $color $hours $minutes",$output);
print_r($output);

?>
