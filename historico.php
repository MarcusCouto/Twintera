<?
	session_start();
	require_once('./engine/conexao.php');
	
	if($_SESSION['logado'] && is_numeric($_SESSION['id_twitter']) && $_SESSION['id_twitter']>0){
		
		$SQL = "SELECT palavra, COUNT(*) as qtd , DATE_FORMAT(data , '%d/%m/%Y %H:%m:%s') as data FROM historico WHERE id_twitter  = ".$_SESSION['id_twitter']." GROUP BY palavra ORDER BY data DESC";	
		$SET = mysql_query($SQL);	
		$num_rows = mysql_num_rows($SET);
		 
		include("./up.php");?>
		
			<div id="site_corpo">
				<div id="corpo">
					<?if($num_rows != 0){?>
					
						<table cellspacing="0" class="">
							<tbody>
								<tr>
									<th>Palavra</th>
									<th>Quantidade</th>
									<th>Data</th>
								</tr>
								<?while($row = mysql_fetch_array($SET)){
									if($row['palavra'] == ""){
										$row['palavra'] = "<em>Em branco</em>";
									}?>
									<tr>
										<td><?=$row['palavra']?></td>
										<td><?=$row['qtd']?></td>
										<td><?=$row['data']?></td>
									</tr>
								<?}?>
							</tbody>
						</table>
					
					<?}else{?>
						<p class="attention">Nenhuma busca foi realizada.</p>
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
