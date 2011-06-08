<?
	require_once('config.php');
	require_once('engine/conexao.php');

 if($_POST){	
 	$SQL = "SELECT DISTINCT u.name AS usuario, COUNT(*) AS qtd FROM posts p INNER JOIN users u ON p.user_id = u.id
	WHERE post LIKE '%".$_POST['busca']."%' GROUP BY p.user_id ORDER BY qtd DESC;";
	$SET = mysql_query($SQL);	
	$num_rows = mysql_num_rows($SET);
	
	
	
	
 
 ?>
 <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"> 
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="pt-br"> 
	<head> 
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" /> 
		<link rel="stylesheet" href="./estilo/estilo.css" type="text/css" /> 
		<link rel="stylesheet" href="./estilo/tabelas.css" type="text/css" /> 
		<title>#twintera!</title> 
	</head> 
	<body> 
	<div id="container">
		<div id="site_corpo">
			<div id="corpo">
				<br /><br />
				<img src="./estilo/images/logo-twintera.jpg" alt="twintera" class="logoGPMH"/>
				<hr/>
				<?
				if($num_rows != 0){
				?>
				<table cellspacing="0" class="gerenciar">	
					<tr>
						<th>Usuário</th>
						<th>Quantidade</th>
					</th>
					<tbody>
				<?
				while($row = mysql_fetch_array($SET)){
					?>
					<tr>
						<td><?=$row['usuario']?></td>
						<td><?=$row['qtd']?></td>
					</tr>
					<?	
				}
				?>
					</tbody>
				</table>
				<?
				}else{
				?><h3>Não existem Twites com a palavra - <?=$_POST['busca']?></h3><?
				}
				?>				
				</form>			
			</div>
		</div>	
	</div>	
	</body> 
</html>
<?
}
?>
