#!/usr/bin/python3
import urllib.request

def fetch_status():
    """Fetches the status from the specified URL and displays the response body."""
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        
    utf8_content = body.decode('utf-8')
    
    print("Body response:")
    print(f"    - type: {type(body)}")
    print(f"    - content: {body}")
    print(f"    - utf8 content: {utf8_content}")

if __name__ == "__main__":
    fetch_status()
