<?php

$message = $_GET['message'];

exec("./python/interface_setRunningMagazine.py $message",$output);
print_r($output);

?>
