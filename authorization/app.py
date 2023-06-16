from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "fhegvjhfgfjcefcghjcfjh"

client = MongoClient('mongodb://localhost:27017/')
db = client['google_authentication']
collection = db['tokens']