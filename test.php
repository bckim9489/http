<?php
	$data = $_POST['parameter1'];
	$data2 = $_POST['parameter2'];
	$comp1 = "data1";
	$comp2 = "data2";
	if($data==$comp1 and $data2 == $comp2){
		echo "Connection Ok!";
	}
	else{
		echo "Error Connection!";
	}
?>
