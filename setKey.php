<?php

$key = $_GET['key'];

exec("./python/setKey.py $key",$output);
print_r($output);

?>
