import requests
from django.conf import settings

def getRole(request):
    access_token = request.headers['Authorization']
    access_token = access_token.split(" ")[1]
    try:
        user = requests.get(settings.AUTH_PATH, headers={"Accept":"*/*", "Authorization": "Bearer " + access_token})
        user = user.json()
    except Exception as e:
        print(e)
        return "Unauthorized"
    
    return user['roles/'][0]