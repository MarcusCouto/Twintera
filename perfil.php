<?
	session_start();
	require_once('config.php');
	require_once('engine/conexao.php');
	
	if($_GET){
		if($_GET['id'] != ""){
			$SQL = "SELECT friends_count, followers_count, profile_image_url, location, screen_name FROM clients WHERE id_twitter =".$_GET['id'].";";	
			$SET = mysql_query($SQL);
			while($row = mysql_fetch_array($SET)){
				$screen_name 		= $row['screen_name'];
				$profile_image_url 	= $row['profile_image_url'];
				$location 			= $row['location'];
				$followers_count 	= $row['followers_count'];
				$friends_count 		= $row['friends_count'];			
			}

			$strig_path ="python get_friends_id.py ".$_SESSION['oauth_token']." ".$_SESSION['oauth_token_secret']." ".$_GET['id'];
			exec($strig_path);
			
		}
	}
?>


<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"> 
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="pt-br"> 
	<head> 
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" /> 
		<link rel="stylesheet" href="./estilo/estilo.css" type="text/css" /> 
		<title>#twintera!</title> 			
	</head> 
	<body> 
	<div id="container">
		<div id="site_corpo">
			<div id="corpo">
				<br /><br />
				<img src="./estilo/images/logo-twintera.jpg" alt="twintera" class="logoGPMH"/>
				<hr/>
				<div>
				<h2><?=$screen_name?></h2>
				<img src="<?=$profile_image_url?>" alt="<?=$screen_name?>"/><br />
				<span>Localização: <?=$location?></span><br/>
				<span>Friends - <?=$friends_count?></span><br/>
				<span>Followers - <?=$followers_count?></span><br/>
				<p>Aguarde um momento enquanto estamos montando sua rede de Amigos...</p>
				</div>						
			</div>
		</div>	
	</div>	
	</body> 
</html>
