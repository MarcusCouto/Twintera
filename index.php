<?
	session_start();
	
	$linkCadastro = "";

	function encode_rfc3986($string){
	   return str_replace('+', ' ', str_replace('%7E', '~', rawurlencode(($string))));
	}
	
	// These values are given to you by Twitter
	// http://twitter.com/oauth
	$consumerSecret = "B3SPTXqFrgW4c4SsqrQlyyXuvQWTzdxyD6S8nI";
	$oauth_consumer_key = "eSWSQWbtOxtj5DJYz9I7dQ";
	
	// The Twitter oauth/request_token method
	$url = "http://twitter.com/oauth/request_token";
	
	// OAuth paramaters
	$oauth_nonce = md5(uniqid(rand(), true));
	$oauth_version = "1.0a";
	$oauth_token = "";
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
	list($oauth_token, $oauth_token_secret) = explode("&", $apiResponse);
	$oauth_token = str_replace("oauth_token=", '', $oauth_token);
	$oauth_token_secret = str_replace("oauth_token_secret=", '', $oauth_token_secret);
	// echo "<h1>HTTP Status Code: $http_code</h1>";
	//echo "<p>$apiResponse</p>";	
	
	$linkCadastro = "<a href=\"http://twitter.com/oauth/authenticate?oauth_token=$oauth_token\">Cadastro</a>";
	
	include("./up.php");
?>
		<div id="site_corpo">
			<div id="corpo">
				<p class="attention">Cadastre-se e monte tamb&eacute;m a sua rede de recomenda&ccedil;&atilde;o.</p>
				<br />
				
				<div id="indexVideo">
					
				</div>
				
				<div id="info">
					
					<div id="infoBusca">
					<p class="attention">Busca</p>
					</div>
					
					
					<div id="infoRede">
					<p class="attention">Rede</p>
					</div>
					
					
					<div id="infoRecomendacao">
					<p class="attention">Recomenda&ccedil;&atilde;o</p>
					</div>
				</div>
			</div>
		</div>	
<?
	include("./down.php");
?>