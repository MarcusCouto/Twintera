<?
	session_start();
	require_once('./engine/conexao.php');
	
	include("./up.php");
	
	if($_POST && $_SESSION['logado']){
	 
		if($_POST['busca'] == ""){?>
			<p class="error">Digite uma palavra no campo de busca.</p>
			<div id="site_corpo">
				<div id="corpo">
					<form action="pesquisa.php" method="post">
					<input type="text" name="busca" class="search"/><br />
					<input type="submit" name="entrar" value="Pesquisar" class="pesquisar"/>
					</form>			
				</div>
			</div>
		<?}else{
		
			$SQL1 = "SELECT friends_count, followers_count, profile_image_url, location, screen_name FROM clients WHERE id_twitter =".$_SESSION['id_twitter'].";";	
			$SET1 = mysql_query($SQL1);
			while($row1 = mysql_fetch_array($SET1)){
				$screen_name1 		= $row1['screen_name'];
				$profile_image_url1 = $row1['profile_image_url'];
				$location1 			= $row1['location'];
				$followers_count1 	= $row1['followers_count'];
				$friends_count1		= $row1['friends_count'];			
			}		
			 
			 
			$SQL = "SELECT COUNT(*)  FROM token  WHERE  token = '".$_POST['busca']."';";
			//echo $SQL ;
			$SET = mysql_query($SQL);	
			$resultados = mysql_result($SET,0);
			
			if($resultados > 0 ){
				$SQL = "SELECT u.id_twitter, u.username, u.profile_image_url, u.friends_count, u.follower_count, u.location, x.qtd, u.statuses_count, u.description, u.url, u.data_criacao FROM users u INNER JOIN (SELECT COUNT(*) as qtd , id_twitter FROM users_token WHERE id_token = (SELECT id FROM token  WHERE  token = '".$_POST['busca']."') GROUP BY id_twitter ORDER BY qtd DESC)x ON u.id_twitter = x.id_twitter";
			
				$SET = mysql_query($SQL);	
				$num_rows = mysql_num_rows($SET);?>
				
					<div id="site_corpo">
						<div id="corpo">
							<h2><?=$screen_name1?></h2>
							<img src="<?=$profile_image_url1?>" alt="<?=$screen_name1?>"/><br />
							<span>Localização: <?=$location1?></span><br/>
							<span>Friends - <?=$friends_count1?></span><br/>
							<span>Followers - <?=$followers_count1?></span><br/>
							<span>Biografia - None</span><br/>
								
							<h3>Resultados com a palavra - <?=$_POST['busca']?></h3>
							
							<?if($_SESSION['logado'] && is_numeric($_SESSION['id_twitter']) && $_SESSION['id_twitter']>0){?>
							<p>Resultado da busca em versão <a href="./gera_exel.php"><em>Excel</em></a></p>
							<?}?>
							
							<?
							while($row = mysql_fetch_array($SET)){
								?>
								<div class="search_result">
									<div class="user_img"><img src="<?=$row['profile_image_url']?>" alt="<?=$row['username']?>"/></div>
									<div class ="user_dados">
										<?=$row['username']?> - <?=$row['qtd']?> Ocorrências <br/>
										<?=$row['location']?><br/>
										<?=$row['description']?><br/>
									</div>
									<div class="user_network">
									Qtd Friends: <?=$row['friends_count']?><br/>
									Qtd Followers: <?=$row['follower_count']?><br/>
									<?
									$SQL = "SELECT text, DATE_FORMAT(criacao_data, '%d/%m/%Y') AS criacao_data FROM posts WHERE users_id = ".$row['id_twitter']." ORDER BY criacao_data DESC LIMIT 1;";
									$BLA = mysql_query($SQL);	
									$num_rows34 = mysql_num_rows($BLA);
									if($num_rows34 != 0){
										while($row34 = mysql_fetch_array($BLA)){
											?>
												<?=$row34['text']?> - <?=$row34['criacao_data']?>
											<?
											
											}
										}
									?>
									<span onclick="javascript: toggle('<?=$row['id_twitter']?>');">Mais...</span>
									</div>
								</div>
								<div class="div_referencias <?=$row['id_twitter']?>">
									<?
									$SQL2 = " SELECT * FROM (SELECT token, COUNT(*) as qtd FROM temp_mention where id_twitter =".$row['id_twitter']."   GROUP BY token)x ORDER BY qtd DESC LIMIT 10;";
									$SETTING = mysql_query($SQL2);	
									$num_rows2 = mysql_num_rows($SETTING);
									if($num_rows2 != 0){
										?>
										<div class="view_mention">
										<ol>
										<?
										while($row2 = mysql_fetch_array($SETTING)){
										?>
											<li><?=$row2['token']?> - <?=$row2['qtd']?></li>						
										<?
										}
										?>
										</ol>
										</div>
										<?						
									}
									$SQL3 = "SELECT * FROM (SELECT token, COUNT(*) as qtd FROM temp_hashtag where id_twitter =".$row['id_twitter']."   GROUP BY token)x ORDER BY qtd DESC LIMIT 10;";
									$SETTING = mysql_query($SQL3);	
									$num_rows3 = mysql_num_rows($SETTING);
									if($num_rows3 != 0){
										?>
										<div class="view_hashtag">
										<ol>
										<?
										while($row3 = mysql_fetch_array($SETTING)){
										?>
											<li><?=$row3['token']?> - <?=$row3['qtd']?></li>						
										<?
										}
										?>
										</ol>
										</div>
										<?
									}
									$SQL4 = "SELECT t.token, x.qtd FROM (SELECT id_token, COUNT(*) as qtd FROM users_token where id_twitter =".$row['id_twitter']." GROUP BY id_token)x INNER JOIN token t ON x.id_token = t.id  ORDER BY qtd DESC LIMIT 10;";
									$SETTING = mysql_query($SQL4);	
									$num_rows4 = mysql_num_rows($SETTING);
									if($num_rows4 != 0){
										?>
										<div class="view_hashtag">
										<ol>
										<?
										while($row4 = mysql_fetch_array($SETTING)){
										?>
											<li><?=$row4['token']?> - <?=$row4['qtd']?></li>						
										<?
										}
										?>
										</ol>
										</div>
										<?
									}
									?>
								</div>
								<?	
							}
							?>			
						</div>
					</div>	
				<?
				include("./down.php");
			}else{
				header("Location:busca_externa.php?q=$_POST['busca']");
				//$strig_path ="python busca_alternativa.py ".$_POST['busca'];
				//exec($strig_path);
			}
		}
	}else{
		$_SESSION['error'] = True;
		$_SESSION['message'] = "Usuário não logado";
		header("Location:index.php");
	}
	include("./down.php");
?>
