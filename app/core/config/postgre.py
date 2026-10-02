import os;
from dotenv import load_dotenv;
from typing import TypedDict;

load_dotenv();

class TPOSTGRE_CONFIG(TypedDict):
    host: str | None
    port: int | None
    user: str | None
    password: str | None
    database: str | None
    
class TPOSTGRE_TABLES(TypedDict):
    USER: str | None
    
POSTGRE_CONFIG: TPOSTGRE_CONFIG = {
    "POSTGRE_HOST": os.getenv("POSTGRE_HOST", None),
    "POSTGRE_PORT": os.getenv("POSTGRE_PORT", None),
    "POSTGRE_USER": os.getenv("POSTGRE_USER", None),
    "POSTGRE_PASSWORD": os.getenv("POSTGRE_PASSWORD", None),
    "POSTGRE_DATABASE": os.getenv("POSTGRE_DATABASE", None) 
}

POSTGRE_TABLES: TPOSTGRE_TABLES = {
    "USER": "user"
}
    
    
    