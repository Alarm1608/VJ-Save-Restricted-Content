import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23518615"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "9af838a204b402f70b8ab9eb402923d6")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://hinditoonteam:7tsxLCnyh9cSchpS@cluster0.qkuhasv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
