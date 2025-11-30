from swiftshadow.classes import ProxyInterface

# Fetch HTTPS proxies from the US
swift = ProxyInterface(countries=["IN"], protocol="https")
print(swift.get().as_string())  # Output: https://<ip>:<port>