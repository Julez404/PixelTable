<?php

$picture = $_GET['picture'];

exec("./python/interface_delPicture.py $picture",$output);
print_r($output);

?>
