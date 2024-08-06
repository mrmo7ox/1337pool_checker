import requests
from logs import logs

def logger(email, password):
    burp0_url = "https://admission.1337.ma:443/api/auth/login"
    burp0_cookies = {"cf_clearance": "MDoP6oVqIQ.iW_KbK97uU2qh37gQSQxkjnD9JMRAIw8-1722976819-1.0.1.1-2JZWXrbhixHMZyt9PdmQYVszm35ox6Oz4Hg..YPMm3qT_h3PGrDPRSeYyltDzMvb8YtF.5jAwSDkdj6Inv8.7g"}
    burp0_headers = {"Sec-Ch-Ua": "\"Chromium\";v=\"121\", \"Not A(Brand\";v=\"99\"", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36", "Sec-Ch-Ua-Arch": "\"\"", "Content-Type": "application/json", "Sec-Ch-Ua-Full-Version": "\"\"", "Accept": "application/json, text/plain, */*", "Sec-Ch-Ua-Platform-Version": "\"\"", "Sec-Ch-Ua-Full-Version-List": "", "Sec-Ch-Ua-Bitness": "\"\"", "Sec-Ch-Ua-Model": "\"\"", "Sec-Ch-Ua-Platform": "\"Windows\"", "Origin": "https://admission.1337.ma", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://admission.1337.ma/en/users/sign_in", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Priority": "u=1, i"}
    burp0_json={"email": str(email), "password": str(password)}
    try:
        response = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies,  json=burp0_json)
        if response.status_code == 201:
            cookies_header = response.headers.get("set-cookie")
            if cookies_header:
                cookies = cookies_header.split(';')
                access_token = None
                for cookie in cookies:
                    if 'accessToken=' in cookie:
                        access_token = cookie.split('accessToken=')[1]
                        break
                if access_token:
                    logs("S",access_token)
                    return access_token
                else:
                    logs("E",'Access Token not found in Set-Cookie header.')
            else:
                logs("E",'No Set-Cookie header found.')
        else:
            logs("E",f"Error making request: {response.status_code}")
    except Exception as e:
        logs("E",f"Error making request: {e}")

