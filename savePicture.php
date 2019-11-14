<?php

$picture = $_GET['picture'];

exec("./python/interface_savePicture.py $picture",$output);
print_r($output);

?>
