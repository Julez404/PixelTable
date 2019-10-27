<?php

$row = $_GET['row'];
$col = $_GET['col'];


print_r($led);
exec("sudo python/main.py $row $col",$output);
print_r($output);

?>
