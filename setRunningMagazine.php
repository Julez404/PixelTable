<?php

$message = $_GET['message'];

exec("./python/setRunningMagazine.py $message",$output);
print_r($output);

?>
