import sys
import ssl

# Ignore SSL certificate errors (required for Bright Data proxies)
ssl._create_default_https_context = ssl._create_unverified_context

proxy_username = "brd-customer-hl_0486f243-zone-isp_proxy1"
proxy_password = "x4kno8n6x37s"

proxy_url = f"http://{proxy_username}:{proxy_password}@brd.superproxy.io:33335"

if sys.version_info[0] == 2:
    import six
    from six.moves.urllib import request
    opener = request.build_opener(
        request.ProxyHandler({
            'http': proxy_url,
            'https': proxy_url
        })
    )
    print(opener.open('http://lumtest.com/myip.json').read())

if sys.version_info[0] == 3:
    import urllib.request
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler({
            'http': proxy_url,
            'https': proxy_url
        })
    )
    print(opener.open('http://lumtest.com/myip.json').read())

#hello wassup
