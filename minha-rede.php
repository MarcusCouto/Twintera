<?
	session_start();
	require_once('./engine/conexao.php');
	
	if($_SESSION['logado'] && is_numeric($_SESSION['id_twitter']) && $_SESSION['id_twitter']>0){
		$SQL = "SELECT s.*, c.users_id FROM clients_users c INNER JOIN users s ON c.users_id = s.id_twitter WHERE c.clients_id =".$_SESSION['id_twitter']." GROUP BY c.users_id";	
		$SET = mysql_query($SQL);	
		$num_rows = mysql_num_rows($SET);
		$quebradelinha = 0;
	 
		include("./up.php");?>
		
			<div id="site_corpo">
				<div id="corpo">
					<?if($num_rows != 0){?>
					
						<table cellspacing="0">
							<tbody>
							<tr>
								<?while($row = mysql_fetch_array($SET)){
									
								$SQL1 = "SELECT friends_count, follower_count, location, description, username FROM users WHERE id_twitter =".$row['users_id'].";";	
								$SET1 = mysql_query($SQL1);
								
								while($row1 = mysql_fetch_array($SET1)){
										$username 			= str_replace(",", " ", $row1['username']);
										$location 			= str_replace(",", " ", $row1['location']);
										$followers_count 	= str_replace(",", " ", $row1['follower_count']);
										$friends_count		= str_replace(",", " ", $row1['friends_count']);			
										$description		= str_replace(",", " ", $row1['description']);
										if($location == "None"){
											$location = "N&atilde;o informado";
										}
										if($description == "None"){
											$description = "N&atilde;o informado";
										}
								}		
								
								$string = "<strong>".$username."</strong><hr/>Localiza&ccedil;&atilde;o: <em>".$location."</em><br/>Descri&ccedil;&atilde;o: <em>".$description."</em><br/>Followers: <em>".$followers_count."</em><br/>Friends: <em>".$friends_count."</em><br/>";
								$quebradelinha++;?>
									<td>
										<a href="http://twitter.com/#!/<?=$row['username']?>" target="_blank" class="tooltip" id="<?=$string?>">
											<img src="<?=$row['profile_image_url']?>" alt="<?=$row['username']?>" width="48px" height="48px"/>
										</a>									
									</td>
									<?if(!($quebradelinha % 16)){?>
										</tr>
										<tr>
									<?}
								}?>
							</tr>
							</tbody>
						</table>
					
					<?}else{?>
						<p class="attention">Voc&ecirc; n&atilde;o possui amigos e seguidores</p>
					<?}?>
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
