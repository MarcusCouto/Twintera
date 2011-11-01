<?
	session_start();
	require_once('./engine/conexao.php');

	if($_SESSION['logado'] && is_numeric($_SESSION['id_twitter']) && $_SESSION['id_twitter']>0){
		//Conta se ha alguma resposta da busca
		$SQL = "SELECT COUNT(*)  FROM token  WHERE  token = '".$_GET['q']."';";
		//echo $SQL ;
		$SET = mysql_query($SQL);	
		$resultados = mysql_result($SET,0);
		
		//Verifica se os dados passados foram passados corretamente
		if($resultados > 0){
			
			//cria o arquivo
			$file = fopen("./excel/excel_".$_SESSION['id_twitter'].".xls", "w+");
			
			//String de escrita no arquivo
			// col1 | col2 | col3 | col4
			$escrita = "Username\tImageURL\tLocation\tFollower Count\tFriends Count\n";
			
			//Selesiona o conteúdo da tabela
			$SQL = "SELECT u.id_twitter, u.username, u.profile_image_url, u.friends_count, u.follower_count, u.location, x.qtd, u.statuses_count, u.description, u.url, u.data_criacao FROM users u INNER JOIN (SELECT COUNT(*) as qtd , id_twitter FROM users_token WHERE id_token = (SELECT id FROM token  WHERE  token = '".$_POST['busca']."') GROUP BY id_twitter ORDER BY qtd DESC)x ON u.id_twitter = x.id_twitter";	
			//echo $SQL;
			
			//itera sobre os dados
			$data = mysql_query($SQL);
			while($row1 = mysql_fetch_array($data)){
				$username		= $row1['username'];
				$profile_image_url 	= $row1['profile_image_url'];
				$location 			= $row1['location'];
				$follower_count 	= $row1['follower_count'];
				$friends_count		= $row1['friends_count'];
				
				$escrita .= $username."\t".$profile_image_url."\t".$location."\t".$follower_count."\t".$friends_count."\n";
			}
			
			//Escreve no arquivo e fecha
			fwrite($file, $escrita);
			fclose($file);
			
			//Redireciona o navegador para o arquivo final
			header("Location:./excel/excel_".$_SESSION['id_twitter'].".xls");
		}else{
			$_SESSION['error'] = True;
			$_SESSION['message'] = "Erro ao capturar usu&aacute;rios";
			header("Location:minha-rede.php");
		}
	}else{
		$_SESSION['error'] = True;
		$_SESSION['message'] = "Usu&aacute;rio n&atilde;o logado";
		header("Location:index.php");
	}
?>