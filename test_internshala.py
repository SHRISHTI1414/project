import requests

url = "https://internshala.com/internships/"

try:
    res = requests.get(url)

    print("Status Code:", res.status_code)
    print("Content Type:", res.headers.get("content-type"))
    print("\nResponse Snippet:\n")
    print(res.text[:500])

except Exception as e:
    print("Error:", e)