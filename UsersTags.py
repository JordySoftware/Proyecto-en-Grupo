import requests
import json

def getTags(user_id):
    url = f"https://api.stackexchange.com/2.2/users/{user_id}/top-tags?site=es.s

    htmlFormat = requests.get(url)
    jsonFormat = htmlFormat.json()
 
  tags = ""
    
  if "error_id" in jsonFormat: 
      return None
  elif not jsonFormat["items"]:
        return "-1"
  else:
    for i in jsonFormat["items"]:
            tags += i["tag_name"] + " "
        tags =tags.replace("-","")
        return tags
