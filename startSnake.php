<?php

$color_snake = $_GET['color_snake'];
$color_apple = $_GET['color_apple'];

exec("./python/interface_startSnake.py $color_snake $color_apple",$output);
print_r($output);

?>
