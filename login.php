<?
	require_once('config.php');
	require_once('engine/conexao.php');

 if($_POST){	
	$SQL = " SELECT COUNT(*) FROM usuario WHERE login = '".$_POST['login']."' AND senha = sha1('".$_POST['password']."');";
	$SET = mysql_query($SQL);
	$number = mysql_result($SET,0);
	
	if($number != 0){
		header("Location: principal.php");	
	}
	else{
	 header("Location: index.php");
	} 
 }
?>
