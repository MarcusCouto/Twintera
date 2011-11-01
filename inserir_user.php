<?
	session_start();	
	require_once('./engine/conexao.php');

	if($_POST){
		extract($_POST);
		
		if($senha == $confirme_senha && $senha != "" && $confirme_senha != ""){				
			
			$QueryUser = "INSERT INTO clients (id, username, senha, inscricao_data, access_token, secret_token, id_twitter) VALUES (DEFAULT,'".$_SESSION['screen_name'] ."', sha1('$senha'),now(),'".$_SESSION['oauth_token']."','".$_SESSION['oauth_token_secret']."','".$_SESSION['id_twitter']."');";	
			mysql_query($QueryUser);
				
			$strig_path ="python user_dados.py ".$_SESSION['oauth_token']." ".$_SESSION['oauth_token_secret']." ".$senha;
			$resultado = system($strig_path, $retval);
			
			$string_redirect ="perfil.php?id=".$_SESSION['user_id'];
			$_SESSION['logado'] = True;
			header("Location: ".$string_redirect);
		}else{
			$_SESSION['logado'] = False;
			$_SESSION['message'] = "Senha ou confirma&ccedil;&atilde;o de senha inv&aacute;lida";
			header("Location: callback.php");	
		}	
	}else{
		$_SESSION['error'] = True;
		$_SESSION['message'] = "Usu&aacute;rio n&atilde;o logado";
		header("Location:index.php");
	}
?>
