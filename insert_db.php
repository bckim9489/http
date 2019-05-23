<?php
	include "dbcon.php";

	$mac = $_POST['mac'];
	$func = $_POST['func'];
	$name = $_POST['name'];
	$img_type = $_POST['img_type'];

	$result = mysqli_query($con,"insert into table values ('$mac','$func','$name','$img_type')"); //num값 알아서넣게
	
	if($result){
		echo "good";
	}
	else{
		echo "bad";
	}
	
 	mysqli_close($con);
?>
