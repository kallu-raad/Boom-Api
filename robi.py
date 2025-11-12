import requests
import json

# code by Jubair bro
url = "https://robiwifi-mw.robi.com.bd/fwa/api/v1/customer/auth/otp/login"

phone_number = input("আপনার ফোন নম্বর দিন (e.g., 01xxxxxxxxx): ")

payload = json.dumps({
  "login": phone_number 
})

headers = {
  'Accept': 'application/json, text/plain, */*',
  'Content-Type': 'application/json',
  'DNT': '1',
  'Referer': 'https://robiwifi.robi.com.bd/',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

try:
    response = requests.request("POST", url, headers=headers, data=payload)
    

    print("\n--- API Response ---")
    print(response.text)
    
   
    try:
        print("\n--- Formatted JSON ---")
        print(json.dumps(response.json(), indent=2))
    except requests.exceptions.JSONDecodeError:
        print("Response-টি JSON ফরম্যাটে নয়।")

except requests.exceptions.RequestException as e:
    print(f"একটি সমস্যা হয়েছে: {e}")