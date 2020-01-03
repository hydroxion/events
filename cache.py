from redis import Redis


# Change the host to '0.0.0.0' if you start the application
# locally
client = Redis(host='redis', port=6379, db=0)
