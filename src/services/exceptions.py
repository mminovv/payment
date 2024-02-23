class RateLimitException(Exception):
    message = "Rate limit exceeded for this user or IP address"

