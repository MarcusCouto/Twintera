<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"> 
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="pt-br"> 
	<head> 
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" /> 
		<link rel="stylesheet" href="./estilo/estilo.css" type="text/css" /> 
		<title>#twintera!</title> 
		<script type="text/javascript" src="./engine/jquery-1.3.2.min.js"></script>
		<script type="text/javascript">
	<!--
		var intContagem = 1;

			$().ready(function()
			{
				
				$('#adicionarContato').click(function() {
					$.ajax({
						type: "POST",
						url: "pesquisa.php",
						data: {busca: "busca"},
						success: function(result){
									$(".resultados").empty();
									$(".resultados").append(result);
								}			
					});
				});				
			
				$(".search").keyup(function(){		
					$.ajax({
						type: "POST",
						url: "pesquisa.php",
						data: {busca: "busca"},
						success: function(result){
									$(".resultados").empty();
									$(".resultados").append(result);
								}			
					});
				
				});
			
			

	-->
	</script>	
	</head> 
	<body> 
	<div id="container">
		<div id="site_corpo">
			<div id="corpo">
				<br /><br />
				<img src="./estilo/images/logo-twintera.jpg" alt="twintera" class="logoGPMH"/>
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
