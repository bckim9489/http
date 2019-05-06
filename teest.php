<?php
	$data = $_POST['parameter1'];
	$data2 = $_POST['parameter2'];
	$comp1 = "data1";
	$comp2 = "data2";
	if($data==$comp1 and $data2==$comp2){
		
		$out = exec('sudo python /var/www/html/rasp_t.py');
		echo $out;
	}
	else{
		echo "non-conn";
	}
?>
