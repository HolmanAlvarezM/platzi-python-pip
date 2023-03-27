import requests

def get_categories():
    req = requests.get("https://api.escuelajs.co/api/v1/categories")
    print(req.status_code)
    print(req.text)
    categories = req.json()
    
    for category in categories:
        print(category['name'])