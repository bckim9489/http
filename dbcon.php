<?php
	$con = mysqli_connect('localhost', 'root', '1q2w3e4r','db');
 
	if (mysqli_connect_errno($con))
	{
	   echo "Failed to connect to MySQL: " . mysqli_connect_error();
	}
	
?>
