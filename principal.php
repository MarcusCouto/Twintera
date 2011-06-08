<?
	// require_once('config.php');
	// require_once('engine/conexao.php');
 	// $SQL = "SELECT DISTINCT u.name AS usuario, COUNT(*) AS qtd FROM posts p INNER JOIN users u ON p.user_id = u.id
	// WHERE post LIKE '%".$_POST['busca']."%' GROUP BY p.user_id ORDER BY qtd DESC;";
	// $SET = mysql_query($SQL);	
	// while()


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
				<a href="./index.php">Sair</a>
				<hr/>
				<form action="pesquisa.php" method="post">
				<fieldset>
				<legend>Pesquisa</legend>
				<input type="text" name="busca" class="search"/><br />
				<input type="submit" name="entrar" value="Pesquisar" class="pesquisar"/>
				</fieldset>
				<div class="resultados">
				</div>
				</form>			
			</div>
		</div>	
	</div>	
	</body> 
</html>
