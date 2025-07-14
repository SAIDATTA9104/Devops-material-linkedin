from flask import Flask, request, jsonify
import mysql.connector
import redis
import os
import json
import logging
from datetime import datetime

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('movie-backend')

# Get environment variables with fallbacks
def get_env_var(name, default=None):
    value = os.getenv(name, default)
    if value is None:
        logger.error(f"Environment variable {name} is not set!")
    return value

# Redis configuration
REDIS_HOST = get_env_var('REDIS_HOST', 'redis')
REDIS_PORT = int(get_env_var('REDIS_PORT', '6379'))
REDIS_DB = int(get_env_var('REDIS_DB', '0'))

# MySQL configuration
DB_HOST = get_env_var('DB_HOST', 'mysql')
DB_USER = get_env_var('DB_USER', 'root')
DB_PASSWORD = get_env_var('DB_PASSWORD', 'moviepass')
DB_NAME = get_env_var('DB_NAME', 'moviemagic')

# Initialize Redis connection pool
redis_pool = redis.ConnectionPool(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    decode_responses=True
)

def get_redis_connection():
    return redis.Redis(connection_pool=redis_pool)

def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        connect_timeout=5
    )

@app.route('/health')
def health_check():
    """Health check endpoint for Kubernetes"""
    try:
        # Test Redis connection
        redis_conn = get_redis_connection()
        redis_conn.ping()
        
        # Test MySQL connection
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1")
        
        return jsonify({
            "status": "healthy",
            "timestamp": datetime.utcnow().isoformat(),
            "components": {
                "redis": "connected",
                "mysql": "connected"
            }
        }), 200
        
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return jsonify({
            "status": "unhealthy",
            "error": str(e)
        }), 500

@app.route('/api/movies', methods=['GET'])
def get_movies():
    """Search movies by title with Redis caching"""
    title = request.args.get('title', '').strip()
    if not title:
        return jsonify({"error": "Title parameter is required"}), 400
    
    logger.info(f"Searching for movies with title: {title}")
    
    redis_conn = get_redis_connection()
    cache_key = f"movie:{title.lower()}"
    
    # Try to get cached results
    try:
        cached_data = redis_conn.get(cache_key)
        if cached_data:
            logger.info(f"Cache hit for {cache_key}")
            return jsonify({
                "source": "cache",
                "cached_at": datetime.utcnow().isoformat(),
                "data": json.loads(cached_data)
            })
    except redis.RedisError as e:
        logger.error(f"Redis error: {str(e)}")
    
    # Query MySQL if not found in cache
    try:
        with get_db_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                query = """
                    SELECT title, year, director, actors, rating 
                    FROM movies 
                    WHERE title LIKE %s AND year >= 2000
                    ORDER BY year DESC
                """
                cursor.execute(query, (f"%{title}%",))
                results = cursor.fetchall()
                logger.info(f"Found {len(results)} movies in database")
                
    except mysql.connector.Error as e:
        logger.error(f"MySQL error: {str(e)}")
        return jsonify({"error": "Database error"}), 500
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "Server error"}), 500
    
    # Cache results if found
    if results:
        try:
            redis_conn.setex(cache_key, 3600, json.dumps(results))
            logger.info(f"Cached results for {cache_key}")
        except redis.RedisError as e:
            logger.error(f"Failed to cache results: {str(e)}")
    
    return jsonify({
        "source": "database",
        "timestamp": datetime.utcnow().isoformat(),
        "count": len(results),
        "data": results or []
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)