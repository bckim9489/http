<?php
	//TODO Delete data2....
	$data = $_POST['parameter1'];
	$data2 = $_POST['parameter2'];
	$comp = "start";
	$out = exec('sudo python /var/www/html/test.py '.$data." ".$data2);
	echo $comp;
?>
