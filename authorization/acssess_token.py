from flask import Flask,redirect,request,session,jsonify
from google_auth_oauthlib import flow
from google.oauth2.credentials import Credentials
from auth_token_flow import authentication_flow
from app import app,collection
import json


@app.route("/")
def get_authentication_url():
    flow = authentication_flow()
    authentication_url , state = flow.authorization_url(
        access_type = "offline",
        prompt = "consent",
        include_granted_scopes = "true"
    )
    
    return redirect(authentication_url)

@app.route("/google_auth")
def get_access_token():
    if request.args.get("error"):
        return "Authorization Not Aproved"
    code = request.args.get("code")
    
    my_flow = authentication_flow()
    my_credentials = my_flow.fetch_token(code = code)
    acsess_token = my_credentials['access_token']
    print("_______________________________",acsess_token)
    id_token = my_credentials['id_token']
    print("_____________________________",id_token)
    refresh_token = my_credentials['refresh_token']
    print("________________________",refresh_token)
    expires_at = my_credentials['expires_at']
    print("_____________________",expires_at)
    scope = my_credentials['scope']
    print("_____________________",scope)
    value = {"acsess_token":acsess_token,"id_token":id_token,"refresh_token":refresh_token,"expires_at":expires_at,"scope":scope}
    result = collection.insert_one(value)
    return jsonify(my_credentials)