<?
    $strServidor	= "localhost";
	$strUsuario 	= "root";
	$strSenha		= "server@bd";
	$strBD			= "mydb";

	// Estabelecendo conex�o com o banco de dados.
	$conn		= mysql_connect($strServidor,$strUsuario,$strSenha) or die ("N�o foi poss�vel conectar ao banco de dados.");
	// Selecionando o banco de dados a ser utilizado pelo sistema.
	mysql_select_db($strBD, $conn)
?>