import os
import redis

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379/0')
conn = redis.from_url(redis_url)
