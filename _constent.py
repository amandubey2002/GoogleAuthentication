#!/usr/bin/python
#
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Various constants used in the Content API for Shopping samples."""

# Constants for configuration
# CONFIG_FILE = 'merchant-info.json'
# TOKEN_FILE = 'stored-token.json'
APPLICATION_NAME = 'Content API for Shopping Samples'

# Constants for authentication
CLIENT_SECRETS_FILE = 'client-secrets.json'
SERVICE_ACCOUNT_FILE = 'service-account.json'

# Constants needed for the Content API
SERVICE_NAME = 'content'
SERVICE_VERSION = 'v2.1'
SANDBOX_SERVICE_VERSION = 'v2.1sandbox'
CONTENT_API_SCOPE = 'https://www.googleapis.com/auth/' + SERVICE_NAME

# These constants define the identifiers for all of our example products/feeds.
#
# The products will be sold online.
CHANNEL = 'online'
# The product details are provided in English.
CONTENT_LANGUAGE = 'en'
# The products are sold in the USA.
TARGET_COUNTRY = 'US'

# Environment variable used for testing against different endpoints.
ENDPOINT_ENV_VAR = 'GOOGLE_SHOPPING_SAMPLES_ENDPOINT'



#merchent-info.json file
MERCHENT_ID = 492080614
MERCHENT_EMAIL = 'amandubey@simprosys.com'

#client-secrete.json file
# CLIENT_ID = '470857629645-1gends290ra65bjk6l93ne8fd7b2qt3e.apps.googleusercontent.com'
CLIENT_ID = '470857629645-371f905mblk11etraf88jhj680elndsp.apps.googleusercontent.com'
PROJECT_ID = 'meta-glazing-389209'
TOKEN_URI = 'https://oauth2.googleapis.com/token'
AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
AUTH_PROVIDER_X509_CERT_URL = 'https://www.googleapis.com/oauth2/v1/certs'
CLIENT_SECRET = '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'
REDIRECT_URIS = ["http://localhost:5000/google_auth"]