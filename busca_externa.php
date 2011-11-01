<?
	session_start();
	require_once('./engine/conexao.php');

	if($_GET){
	
		$strig_path ="python busca_externa.py ".$_GET['q'];
		exec($strig_path);
		
		include("./up.php");
		
		$QueryUser = "SELECT friends_count, followers_count, profile_image_url, location, screen_name FROM clients WHERE id_twitter =".$_SESSION['id_twitter'].";";	
		$ResultUser = mysql_query($QueryUser);
		while($row_user = mysql_fetch_array($ResultUser)){
			$screen_name1 		= $row_user['screen_name'];
			$profile_image_url1 = $row_user['profile_image_url'];
			$location1 			= $row_user['location'];
			$followers_count1 	= $row_user['followers_count'];
			$friends_count1		= $row_user['friends_count'];			
		}
		
		$QueryWord = "SELECT * FROM busca_externa WHERE word = '".$_GET['q']."'";
		$ResultWord = mysql_query($QueryWord);	
		?>
		
		<div id="site_corpo">
			<div id="corpo">
				<h2><?=$screen_name1?></h2>
				<img src="<?=$profile_image_url1?>" alt="<?=$screen_name1?>"/><br />
				<span>Localização: <?=$location1?></span><br/>
				<span>Friends - <?=$friends_count1?></span><br/>
				<span>Followers - <?=$followers_count1?></span><br/>
				<span>Biografia - None</span><br/>
				<p class="attention">N&atilde;o foram encontrados resultados para essa palavra -  <?=$_GET['q']?>.</p>
				<p class="attention">Seguem algumas sugestões da base doTwitter. Brevemente estaremos<br/><br/> disponibilizando esta palavra também em nossa base. </p>
				<?
				while($row_word = mysql_fetch_array($ResultWord)){
					?>
					<div class="search_result">
						<div class="user_img"><img src="<?=$row_word['profile_image_url']?>" alt="<?=$row_word['username']?>"/></div>
						<div class ="user_dados"><?=$row_word['username']?> </div>
						<iframe allowtransparency="true" frameborder="0" scrolling="no" src="http://platform.twitter.com/widgets/follow_button.html?screen_name=<?=$row_word['username']?>&lang=pt" style="width:300px; height:20px;"></iframe>
					</div>				
				 <?} ?>	
			</div>
		</div>							
		<?		
		include("./down.php");
		
	}else{
		$_SESSION['error'] = True;
		$_SESSION['message'] = "Digite uma palavra na busca";
		header("Location: pesquisa.php");
	}
	
?>
