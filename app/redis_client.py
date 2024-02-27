import redis
from typing import Optional

class RedisClient:
    def __init__(self, host: str = 'localhost', port: int = 6379, db: int = 0, password: Optional[str] = None):
        self._client = redis.Redis(host=host, port=port, db=db, password=password, decode_responses=True)

    def set_value(self, key: str, value: str) -> bool:
        """Set a value in Redis."""
        return self._client.set(key, value)

    def get_value(self, key: str) -> Optional[str]:
        """Get a value from Redis."""
        return self._client.get(key)
