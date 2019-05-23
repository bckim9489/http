<?php
function oddstarQuery($query){
	global $con;
	$result =  mysqli_query($con,$query);	

	return $result;
}
function oddstarArray($result,$type="MYSQL_ASSOC"){
	return mysqli_fetch_array($result);
}
function oddstarAssoc($result){
	return mysqli_fetch_assoc($result);
}
function oddstarRows($result){
	return mysqli_num_rows($result);
}
function oddstarInsert($table, $array){
	foreach($array as $key => $value ){
		$set[]= $key;
		$values[]=$value;
	}
	$sql = "INSERT INTO ".$table." (".implode(",",$set).") VALUES (".implode(",",$values).")";
	$result = oddstarQuery($sql);
	return $result;
}
function oddstarUpdate($table,$array,$where="1"){
	$sql = "update ".$table." set ";
	foreach($array as $key => $value ){
		$sql .= $key."=".$value.",";
	}
	$sql = substr($sql, 0, -1);
	$sql .=" where ".$where;
	$result = oddstarQuery($sql);
	return $result;
}
?>
