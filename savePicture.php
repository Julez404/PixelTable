<?php

$picture = $_GET['$picture'];

exec("./python/savePicture.py $picture",$output);
print_r($output);

?>
