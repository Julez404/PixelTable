<?php

$picture = $_GET['picture'];

exec("./python/setPicture.py $picture",$output);
print_r($output);

?>
