<?php

	session_start();
	require_once('config.php');
	function encode_rfc3986($string)
	{
	   return str_replace('+', ' ', str_replace('%7E', '~', rawurlencode(($string))));
	}
	
	$oauth_consumer_key = "eSWSQWbtOxtj5DJYz9I7dQ";
	$consumerSecret = "B3SPTXqFrgW4c4SsqrQlyyXuvQWTzdxyD6S8nI";
	
	// The Twitter oauth/access_token method
	$url = "http://twitter.com/oauth/access_token";
	
	// OAuth paramaters
	$oauth_nonce = md5(uniqid(rand(), true));
	$oauth_version = "1.0a";
	$oauth_token = $_GET['oauth_token'];
	$oauth_timestamp = time();
	$oauth_signature_method = "HMAC-SHA1";
	
	// Create $oauth_signature
	// First concatenate all parameters except oauth_signature
	$parametersSoFar = "oauth_consumer_key=$oauth_consumer_key&" .
	"oauth_nonce=$oauth_nonce&" .
	"oauth_signature_method=$oauth_signature_method&" .
	"oauth_timestamp=$oauth_timestamp&" .
	"oauth_token=$oauth_token&" .
	"oauth_version=$oauth_version";
	
	// Next encode them to OAuth spec
	$encodedParams = encode_rfc3986($parametersSoFar);
	
	// Next create your signature base string
	$signatureBaseString = "GET&" . encode_rfc3986($url) . "&" . 
	$encodedParams;
	
	// Next create your key, hash your signature base string, and encode the new parameter
	$key = "$consumerSecret&$oauth_token";
	$oauth_signature = encode_rfc3986(base64_encode(hash_hmac('sha1',$signatureBaseString, $key, true)));
	
	// Now create your Authorization Header with all of your parameters
	$authorizationHeader = "Authorization: OAuth oauth_consumer_key=\"$oauth_consumer_key\",
	oauth_token=\"$oauth_token\",
	oauth_nonce=\"$oauth_nonce\",
	oauth_timestamp=\"$oauth_timestamp\",
	oauth_signature_method=\"$oauth_signature_method\",
	oauth_version=\"$oauth_version\",
	oauth_signature=\"$oauth_signature\"";
	
	$_header[] = 'Expect:';
	$_header[] = $authorizationHeader;
	
	// GET Twitter API results using cURL
	$curlHandle = curl_init();
	curl_setopt($curlHandle, CURLOPT_URL, "$url");
	curl_setopt($curlHandle, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($curlHandle, CURLOPT_HTTPHEADER, $_header);
	$apiResponse = curl_exec($curlHandle);
	
	// Get HTTP Code
	$info = curl_getinfo($curlHandle);
	$http_code = $info['http_code'];
	
	// Close cURL connection
	curl_close($curlHandle);
	
	// The tokens are returned in the body of the cURL response
	// Dig them out here
	list($oauth_token, $oauth_token_secret, $user_id, $screen_name) = explode("&",$apiResponse);
	$oauth_token = str_replace("oauth_token=", '', $oauth_token);
	$oauth_token_secret = str_replace("oauth_token_secret=", '', $oauth_token_secret);
	$user_id = str_replace("user_id=", '', $user_id);
	$screen_name = str_replace("screen_name=", '', $screen_name);
	// echo "<h1>HTTP Status Code: $http_code</h1>";
	// echo "<p>$apiResponse</p>";
	
	
	
	// Token parameters
	// echo "<p>OAuth Token: parameter: $oauth_token</p>";
	// echo "<p>OAuth Token Secret: parameter: $oauth_token_secret</p>";
		
	$conteudo = "\r\n token = ".$oauth_token." , secret_token = ".$oauth_token_secret." ;";	
	
	
	// include 'EpiCurl.php';
	// include 'EpiOAuth.php';
	// include 'EpiTwitter.php';
	
	$consumer_key = 'eSWSQWbtOxtj5DJYz9I7dQ';
	$consumer_secret = 'B3SPTXqFrgW4c4SsqrQlyyXuvQWTzdxyD6S8nI';

	$filename = 'login.txt';

		if (!$handle = fopen($filename, 'a')) {
			 echo "Não foi possível abrir o arquivo ($filename)";
			 exit;
		}

		if (fwrite($handle, $conteudo) === FALSE) {
			echo "Não foi possível escrever no arquivo ($filename)";
			exit;
		}
		
	fclose($handle);
	
	$_SESSION['oauth_token'] = $oauth_token;
	$_SESSION['oauth_token_secret'] = $oauth_token_secret;
	$_SESSION['user_id'] = $user_id;
	
	
	// echo $oauth_token."<br />";
	// echo $oauth_token_secret."<br />";	
	// echo $user_id."<br />";	
	// echo $screen_name."<br />";	
 
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
			<hr/>
			<p>Cadastre seu login e senha de acesso ao #twintera!<br />Come ele você poderá acessar nossos serviços.
			<form action="inserir_user.php" method="post">
			<fieldset>
			<legend>Cadastre uma senha </legend>
			<label>Senha<label><br />
			<input type="password" name="senha"/><br />
			<label>Confirmar senha<label><br />
			<input type="password" name="confirme_senha"/><br />
			<input type="submit" name="entrar" Value="Entrar"/>
			</fieldset>
			</form>
			</div>
		</div>	
	</div>	
	</body> 
</html>