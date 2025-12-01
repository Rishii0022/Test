from swiftshadow.classes import ProxyInterface

# Fetch HTTPS proxies from the US
swift = ProxyInterface(countries=["in"], protocol="https")
print(swift.get().as_string())  # Output: https://<ip>:<port>
