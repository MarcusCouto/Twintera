<?
	session_start();
	require_once('./engine/conexao.php');
	
	
	if($_SESSION['logado']){
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
				
			}
		}?>
		
		<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"> 
		<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="pt-br"> 
			<head> 
				<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" /> 
				<link rel="stylesheet" href="./estilo/estilo.css" type="text/css" />
				
				<title>#twintera!</title> 
				<script type="text/javascript" src="./engine/jquery-1.6.4.min.js" ></script>
				<script type="text/javascript" src="./engine/tooltip.jquery.js" ></script>
				<script type="text/javascript">
					$(document).ready(function(){
						$('.tooltip').tooltip();
					});
				</script> 
			</head> 
			<body> 
			<div id="content">
				<h1 id="logo"><span>#twintera!</span></h1>
				<ul id="menu">
					<li>&nbsp;</li>
					<li>&nbsp;</li>
					<li>&nbsp;</li>
					<li>&nbsp;</li>
					<li>&nbsp;</li>
				</ul>
				
				<?if(isset($_SESSION['error']) && $_SESSION['error'] == True && $_SESSION['message'] != ""){?>
					<p class="error"><?=$_SESSION['message']?></p>
					
				<?
					$_SESSION['error'] = False;
					$_SESSION['message'] = "";
				}?>
					<div id="site_corpo">
						<div id="corpo">
							<div>
								<p class="attention">Aguarde um momento enquanto estamos montando sua rede de Amigos...</p>	
								<h2><?=$screen_name?></h2>
								<img src="<?=$profile_image_url?>" alt="<?=$screen_name?>"/><br />
								<span>Localiza&ccedil;&atilde;o: <?=$location?></span><br/>
								<span>Friends - <?=$friends_count?></span><br/>
								<span>Followers - <?=$followers_count?></span><br/>	
							</div>						
						</div>
					</div>	
<?
	}else{
		$_SESSION['error'] = True;
		$_SESSION['message'] = "Usu&aacute;rio n&atilde;o logado";
		header("Location:index.php");
	}
	include("./down.php");
?>


