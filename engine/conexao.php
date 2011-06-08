<?
    $strServidor	= "localhost";
	$strUsuario 	= "root";
	$strSenha		= "server@bd";
	$strBD			= "mydb";

	// Estabelecendo conexão com o banco de dados.
	$conn		= mysql_pconnect($strServidor,$strUsuario,$strSenha) or die ("Não foi possível conectar ao banco de dados.");
	// Selecionando o banco de dados a ser utilizado pelo sistema.
	mysql_select_db($strBD, $conn);
?>
