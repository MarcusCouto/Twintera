<?
	session_start();
	require_once('./engine/conexao.php');

	if($_GET){
	
		$strig_path ="python busca_alternativa.py ".$_GET['q'];
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
		
		$QueryWord = "SELECT u.id_twitter, u.username, u.profile_image_url, u.friends_count, u.follower_count, u.location, x.qtd, u.statuses_count, u.description, u.url, u.data_criacao FROM users u INNER JOIN (SELECT COUNT(*) as qtd , id_twitter FROM users_token WHERE id_token = (SELECT id FROM token  WHERE  token = '".$_GET['q']."') GROUP BY id_twitter ORDER BY qtd DESC)x ON u.id_twitter = x.id_twitter";
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
				<h3>Resultados com a palavra - <?=$_GET['q']?></h3>
				<?
				while($row_word = mysql_fetch_array($ResultWord)){
					?>
					<div class="search_result">
						<div class="user_img"><img src="<?=$row_word['profile_image_url']?>" alt="<?=$row_word['username']?>"/></div>
						<div class ="user_dados">
							<?=$row_word['username']?> - <?=$row_word['qtd']?> Ocorrências <br/>
							<?=$row_word['location']?><br/>
							<?=$row_word['description']?><br/>
						</div>
						<div class="user_network">
						Qtd Friends: <?=$row_word['friends_count']?><br/>
						Qtd Followers: <?=$row_word['follower_count']?><br/>
						<?
						$QueryLastPost = "SELECT text, DATE_FORMAT(criacao_data, '%d/%m/%Y') AS criacao_data FROM posts WHERE users_id = ".$row['id_twitter']." ORDER BY criacao_data DESC LIMIT 1;";
						$ResultLastPost = mysql_query($QueryLastPost);	
						$NumberPosts = mysql_num_rows($ResultLastPost);
						if($NumberPosts != 0){
							while($row_posts = mysql_fetch_array($ResultLastPost)){
								echo $row_posts['text']." - ".$row_posts['criacao_data'];
							}
						}
						?>
						<span onclick="javascript: toggle('<?=$row_word['id_twitter']?>');">Mais...</span>
						</div>
					</div>
					<div class="div_referencias <?=$row_word['id_twitter']?>">
						<?
						$QueryMention = " SELECT * FROM (SELECT token, COUNT(*) as qtd FROM temp_mention where id_twitter =".$row['id_twitter']."   GROUP BY token)x ORDER BY qtd DESC LIMIT 10;";
						$ResultMention = mysql_query($QueryMention);	
						$NumberMentions = mysql_num_rows($ResultMention);
						if($NumberMentions != 0){?>
							<div class="view_mention">
								<ol><?
								while($row_mention = mysql_fetch_array($ResultMention)){
									?><li><?=$row_mention['token']?> - <?=$row_mention['qtd']?></li><?
								}
								?></ol>
							</div><?						
						}
						
						$QueryHashtag = "SELECT * FROM (SELECT token, COUNT(*) as qtd FROM temp_hashtag where id_twitter =".$row['id_twitter']."   GROUP BY token)x ORDER BY qtd DESC LIMIT 10;";
						$ResultHashtag = mysql_query($QueryHashtag);	
						$NumberHashtag = mysql_num_rows($ResultHashtag);
						if($NumberHashtag != 0){?>
							<div class="view_hashtag">
								<ol><?
								while($row3 = mysql_fetch_array($ResultHashtag)){
									?><li><?=$row3['token']?> - <?=$row3['qtd']?></li><?
								}
								?></ol>
							</div><?
						}
						
						$QueryTopToken = "SELECT t.token, x.qtd FROM (SELECT id_token, COUNT(*) as qtd FROM users_token where id_twitter =".$row['id_twitter']." GROUP BY id_token)x INNER JOIN token t ON x.id_token = t.id  ORDER BY qtd DESC LIMIT 10;";
						$ResultTopToken = mysql_query($QueryTopToken);	
						$NumberTopToken = mysql_num_rows($ResultTopToken);
						if($NumberTopToken != 0){?>
							<div class="view_hashtag">
								<ol><?
								while($row4 = mysql_fetch_array($ResultTopToken)){
									?><li><?=$row4['token']?> - <?=$row4['qtd']?></li><?
								}
								?></ol>
							</div><?
						}
						?>
					</div><?	
				}?>	
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
