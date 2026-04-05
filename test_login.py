import requests

session = requests.Session()

login_url = "https://internshala.com/login/"

try:
    res = session.get(login_url)

    print("Login Page Status:", res.status_code)
    print("\nResponse Snippet:\n")
    print(res.text[:500])

except Exception as e:
    print("Error:", e)
    