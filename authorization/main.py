from flask import Flask
from acssess_token import get_authentication_url
from app import app


get_authentication_url()

if __name__ == "__main__":
    app.run(debug=True, ssl_context=('cert.pem', 'priv_key.pem'))


