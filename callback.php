<?
	session_start();
	
	function encode_rfc3986($string){
	   return str_replace('+', ' ', str_replace('%7E', '~', rawurlencode(($string))));
	}
	
	if(!isset($_SESSION['oauth_token']) || !isset($_SESSION['oauth_token_secret'])){
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
		list($oauth_token, $oauth_token_secret, $user_id, $screen_name) = explode("&", $apiResponse);
		$oauth_token = str_replace("oauth_token=", '', $oauth_token);
		$oauth_token_secret = str_replace("oauth_token_secret=", '', $oauth_token_secret);
		$user_id = str_replace("user_id=", '', $user_id);
		$screen_name = str_replace("screen_name=", '', $screen_name);

		$conteudo = "\r\n token = ".$oauth_token." , secret_token = ".$oauth_token_secret." ;";	

		$consumer_key = 'eSWSQWbtOxtj5DJYz9I7dQ';
		$consumer_secret = 'B3SPTXqFrgW4c4SsqrQlyyXuvQWTzdxyD6S8nI';

		$_SESSION['screen_name'] = $screen_name;
		$_SESSION['oauth_token'] = $oauth_token;
		$_SESSION['oauth_token_secret'] = $oauth_token_secret;
		$_SESSION['user_id'] = $user_id;
		$_SESSION['id_twitter'] = $user_id;
	}

	include("./up.php");
?>
		<div id="site_corpo">
			<div id="corpo">
			<p class="attention">Cadastre seu login e senha de acesso ao #twintera!<br /><br />Com ele voc&ecirc; poder&aacute; acessar nossos servi&ccedil;os.</p>
			<form action="inserir_user.php" method="post">
			<label>Senha</label><br />
			<input type="password" name="senha"/><br /><br />
			<label>Confirmar senha</label><br />
			<input type="password" name="confirme_senha"/><br />
			<input type="submit" name="entrar" Value="Entrar"/>
			</form>
			</div>
		</div>	
<?
	include("./down.php");
?>
