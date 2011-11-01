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
			<?if(isset($_SESSION['logado'])){?>
				<li><a href="#">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a></li>
				<li><a href="./pesquisa.php">Pesquisa</a></li>
				<li><a href="./minha-rede.php">Minha Rede</a></li>
				<li><a href="./historico.php">Hist&oacute;rico de Busca</a></li>
				<li><a href="./logout.php">Sair</a></li>
			<?}else{?>
				<?if(isset($linkCadastro)){?>
					<li id="cadastro"><?=$linkCadastro?></li>
					<li style="margin:0px 0px 0px 200px;">
						<div>
						<form action="login.php" method="post" style="height:40px;">
						<label>Username</label>
						<input type="text" name="login" style="width:90px;"/>
						<label>Senha</label>
						<input type="password" name="password" style="width:90px;"/>
						<input type="submit" name="entrar" Value="Entrar" style="margin-top:5px;"/>
						</form>
						</div>
					</li>
				<?}
			}?>
		</ul>
		
		<?if(isset($_SESSION['error']) && $_SESSION['error'] == True && $_SESSION['message'] != ""){?>
			<p class="error"><?=$_SESSION['message']?></p>
			
		<?
			$_SESSION['error'] = False;
			$_SESSION['message'] = "";
		}?>
		
