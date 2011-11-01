<?
	session_start();
	require_once('./engine/conexao.php');

	if($_POST){
		
		if($_POST['login'] == "" || $_POST['password'] == ""){
			$_SESSION['error'] = True;
			$_SESSION['message'] = "Campo Username ou Senha em branco";
			header("Location:index.php");
		}else{
			$SQL = " SELECT COUNT(*) FROM clients WHERE username = '".$_POST['login']."' AND senha = sha1('".$_POST['password']."');";
			$SET = mysql_query($SQL);
			$number = mysql_result($SET,0);

			if($number != 0){
				$SQL = " SELECT id_twitter FROM clients WHERE username = '".$_POST['login']."' AND senha = sha1('".$_POST['password']."');";
				$SET = mysql_query($SQL);
				$_SESSION['id_twitter'] = mysql_result($SET,0);
				$_SESSION['logado'] = True;
				header("Location:pesquisa.php");	
			}
			else{
				$_SESSION['error'] = True;
				$_SESSION['message'] = "Username ou Senha inv&aacute;lidos";
				header("Location:index.php");
			} 
		}
		
	}else{
		$_SESSION['error'] = True;
		$_SESSION['message'] = "Usu&aacute;rio n&atilde;o logado";
		header("Location:index.php");
	}
?>
