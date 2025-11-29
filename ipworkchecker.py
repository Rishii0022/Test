import requests

proxy = "219.65.73.81:80"

proxies = {
    "http": f"http://{proxy}",
    "https": f"http://{proxy}"
}

try:
    response = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=5)
    print("Proxy is working")
    print("Response:", response.json())
except Exception as e:
    print("Proxy failed")
    print("Error:", e)
