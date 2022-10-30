import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5620374374:AAFYDge2vy7RMNsGsnJJP7d6qnba8tHV6Go")
    
    API_ID = int(os.environ.get("API_ID", 18000552))
    
    API_HASH = os.environ.get("4fc429f67c0543a6f24134cc35851dd4")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "1647611573"))

    SESSION_NAME = "urluploadjoebot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://uploadbotv2:Ichbinschwul2@cluster0.6eyjorl.mongodb.net/?retryWrites=true&w=majority")

    MAX_RESULTS = "50"
