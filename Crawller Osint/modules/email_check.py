import requests

def check_email_leaks(email, api_key):
    headers = {
        "hibp-api-key": api_key,
        "user-agent": "OSINT-Crawler"
    }
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"

    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return response.json()  
        elif response.status_code == 404:
            return []
        else:
            return {"error": response.status_code}
    except Exception as e:
        return {"error": str(e)}
