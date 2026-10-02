from pymongo import AsyncMongoClient;
from app.core.connection.mongodb import MONGODB_CONFIG;

if MONGODB_CONFIG["MONGODB_URL"] is None:
    raise RuntimeError("No MONGODB_URL found");

if MONGODB_CONFIG["MONGODB_DB_NAME"] is None:
    raise RuntimeError("No MONGODB_DB_NAME found");

MONGODB_CLIENT: AsyncMongoClient = AsyncMongoClient(
    MONGODB_CONFIG["MONGODB_URL"]
)

MONGODB_DATABASE = MONGODB_CLIENT[MONGODB_CONFIG["MONGODB_DB_NAME"]];


