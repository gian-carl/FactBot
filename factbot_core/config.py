# Configuration settings for FactBot

# Credibility scores: how much we trust each source (0.0 = not trusted, 1.0 = very trusted)
CREDIBILITY_SCORES = {
    "wikipedia": 0.5,      
    "newsapi": 0.7,        # News API – generally reliable
    "fallback": 0.3        # Fallback – only used if others fail
}

# API keys 
NEWS_API_KEY = ""          

# File paths for logs and cache
LOG_FILE = "factbot_logs.json"
CACHE_FILE = "factbot_cache.json"

# How many past questions and answers to remember (context memory)
CONTEXT_SIZE = 3

# Timeout for internet requests (seconds)
TIMEOUT = 5

# How many threads to use for parallel fetching
MAX_WORKERS = 4