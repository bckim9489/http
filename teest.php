<?php
	$data = $_POST['parameter1'];
	$data2 = $_POST['parameter2'];
	$comp = "start";
	$out = exec('sudo python /var/www/html/test.py '.$data);
	echo $out;
?>
