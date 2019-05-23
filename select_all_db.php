<?php
	include "dbcon.php";

	$result = mysqli_query($con,"select * from table");

	if($result){		
	 	$return_array = array();
		$index_array = array();
		
		for($i=0; $i<mysqli_num_fields($result); $i++){
			$index_array[$i] = mysqli_fetch_field_direct($result,$i);
		}
	 	
		while($row = mysqli_fetch_array($result))
			{
			for($i=0; $i<mysqli_num_fields($result); $i++){
				$tmp = $index_array[$i];
				$row_array[$tmp->name] = $row[$i];
			}
			array_push($return_array,$row_array);		
		}

		echo json_encode(array("result"=>$return_array));

	}
 	else {
 		echo mysqli_error($con);
 	}

	mysqli_close($con);

?>