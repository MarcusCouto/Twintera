<?
    $strServidor	= "twintera.no-ip.info";
	$strUsuario 	= "root";
	$strSenha		= "server@bd";
	$strBD			= "mydb";

	// Estabelecendo conex„o com o banco de dados.
	$conn = mysql_connect($strServidor,$strUsuario,$strSenha);
	if(!$conn){
		$_SESSION['error'] = True;
		$_SESSION['message'] = "N&atilde;o foi poss&iacute;vel conectar ao banco de dados.";
		header("Location:index.php");
	}
	// Selecionando o banco de dados a ser utilizado pelo sistema.
	mysql_select_db($strBD, $conn) or die(mysql_error())
?>