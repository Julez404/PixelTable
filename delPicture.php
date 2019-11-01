<?php

$picture = $_GET['picture'];

exec("./python/delPicture.py $picture",$output);
print_r($output);

?>
