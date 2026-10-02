import os;
from dotenv import load_dotenv;
from typing import TypedDict;

class TMONGODB_CONFIG(TypedDict):
    MONGODB_URL: str | None
    MONGO_DB_NAME: str | None
    
class TMONGODB_COLLECTIONS(TypedDict):
    USERS: str
    CLIENTS: str

MONGODB_CONFIG: TMONGODB_CONFIG = {
    "MONGODB_URL": os.getenv("MONGODB_URL", None),
    "MONGODB_DB_NAME": os.getenv("MONGODB_DB_NAME", None)
}

MONGODB_COLLECTIONS: TMONGODB_COLLECTIONS = {
    "USERS": "users",
    "CLIENTS": "clients"
}

