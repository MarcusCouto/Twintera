# -*- coding: utf-8 -*-

import twitter
import json


t = twitter.Twitter(domain='api.twitter.com', api_version='1')
response = t.users.show(user_id=20318677)
print json.dumps(response, sort_keys=True, indent=4)
