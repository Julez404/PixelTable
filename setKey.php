<?php

$key = $_GET['key'];

exec("./python/interface_setKey.py $key",$output);
print_r($output);

?>
