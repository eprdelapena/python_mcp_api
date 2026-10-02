from typing import Any, Protocol

from app.core.connection.mongodb import (
    MONGODB_DATABASE,
    MONGODB_COLLECTIONS,
)

class PUserRepository(Protocol):
    @staticmethod
    async def find_by_id(user_id: str) -> dict[str, Any] | None:
        ...
        
    @staticmethod
    async def find_by_username(username: str) -> dict[str, Any] | None:
        ...
        
    @staticmethod
    async def find_by_email(email: str) -> dict[str, Any] | None:
        ...
    
    
class UserRepository(PUserRepository):
    @staticmethod
    async def find_by_id(user_id: str) -> dict[str, Any] | None:
        user: dict[str, Any] | None = None;
        query = await MONGODB_DATABASE[MONGODB_COLLECTIONS["USERS"]].find_one({"_id": user_id});
        
        if query:
            user = query;
            
        return user;