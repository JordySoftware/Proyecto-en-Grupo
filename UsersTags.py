import requests
import json

def getTags(user_id):
url = f"https://api.stackexchange.com/2.2/users/{user_id}/top-tags?site=es.s
