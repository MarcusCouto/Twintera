from time import time
from random import getrandbits
from time import time
import urllib
import urllib2
import hashlib
import hmac
import json

class twintera(Auth):
	"""
    An Twintera authenticator.
    """
    def __init__(self, token, token_secret, consumer_key, consumer_secret):
        """
        Create the authenticator. If you are in the initial stages of
        the Twintera dance and don't yet have a token or token_secret,
        pass empty strings for these params.
        """
        self.token = token
        self.token_secret = token_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret

    def encode_params(self, base_url, method, params):
        params = params.copy()

        if self.token:
            params['oauth_token'] = self.token

        params['oauth_consumer_key'] = self.consumer_key
        params['oauth_signature_method'] = 'HMAC-SHA1'
        params['oauth_version'] = '1.0'
        params['oauth_timestamp'] = str(int(time()))
        params['oauth_nonce'] = str(getrandbits(64))

        enc_params = urlencode_noplus(sorted(params.iteritems()))

        key = self.consumer_secret + "&" + urllib.quote(self.token_secret, '')

        message = '&'.join(
            urllib.quote(i, '') for i in [method.upper(), base_url, enc_params])

        signature = hmac.new(
            key, message, hashlib.sha1).digest().encode('base64')[:-1]
        return enc_params + "&" + "oauth_signature=" + urllib.quote(signature, '')

    def generate_headers(self):
        return {}
		
	def conexao():	