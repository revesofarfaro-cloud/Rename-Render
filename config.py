# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "11617513")

API_HASH = os.environ.get("API_HASH", "1c4e6108c7939d56b02290a336fc9d81")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8094671010:AAGdBX9G353bff7gGp4MKQ6PVoYtKKnQN3Y") 

FORCE_SUB = os.environ.get("FORCE_SUB", "An1Samuray") 

             # Don't Remove Credit @An1Samuray
             # Subscribe YouTube Channel For Amazing Bot @An1Samuray
             # Ask Doubt on telegram @An1Samuray

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://revesofarfaro:vzzqbnW1CIsK9gP6@cluster0.hntyh5h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5955835550').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
