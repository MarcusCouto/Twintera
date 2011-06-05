<?
session_start();	

if($_POST){		
	
	$login				= $_POST['login']; 
	$senha				= $_POST['senha']; 
	$confirme_senha		= $_POST['confirme_senha'];
	
	if($senha == $confirme_senha){	
		$strig_path ="python user_dados.py ".$_SESSION['oauth_token']." ".$_SESSION['oauth_token_secret']." ".$senha;
		exec($strig_path);
		$string_redirect ="perfil.php?id=".$_SESSION['user_id'];	
		header("Location: ".$string_redirect);
	}else{
		header("Location: ".$string_redirect);	
	}			
 } 
?>