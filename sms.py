import requests
import json
import random

session = requests.Session()

otp_url = "https://gateway.most.gov.bd/auth/oauth/send-otp"

headers = {
    'Accept': 'application/json',
    'Authorization': '',
    'Content-Type': 'application/json',
    'DNT': '1',
    'Referer': 'https://services.most.gov.bd/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/5.37.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/5.37.36',
    'X-Api-Key': '4rhwlff8q4q860qsb9utv73x12nua8h7',
    'X-App-Identifier': 'SecurityUI',
    'X-Client-Id': '75b4b010fde64b1aace9d46f3c1880d5',
    'X-Client-Secret': '7a169F9B0F4f4350Ad1a430ce4F9d215',
    'X-Device-Id': '17f1e8348d39d81762945688271',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}
# code by Jubair bro

user_phone = input("Your phone number (Phone): ")

fake_email = f"user{random.randint(10000, 99999)}@example.com"
print(f"Using fake email: {fake_email}")

payload = {
    "name": "Md jubair Ahmed",
    "email": fake_email,
    "phone": user_phone,
    "registration_type": 1,
    "captcha_token": "511fb2f2ed6211d2a471a7af9a0fa140",
    "recaptcha_token": "0cAFcWeA6rJmbagozahVZSHL3qiQZUv9-Odc2NUcdYHBbguBvy_1y3qYTikIKSwXokvN3XvIxZ6cGm-Eyqg3_nB4G6VP1MIKfdMxg5mwvgKexSFwNOdaZcPtRhOZfnecXEbrlsbFsP9g7JDiviPka-q_gdSxaq_8lONc3oFneggFhmF2pQUpNW2Wj3qTMtypIEcJDRb_7FTICOX59HhFH8DaakMZ1JLSvC-GjsEN1uKu58SaXowDgifiPnPLCSy4pF6S_8XwdyrtmR6m8jxsJvMrqDXlqkrdhj5DPoCWxeCwyzpb3JfjtZm643dCJxAlT-GMz1sQew99r8_zbePD42Tq5MU9uY87TqyEqNlsRDmzwtZdRk3ouJ1WZqsGgSD6B0ISp_63fufBC97cqTKfT3nvBNsEFjcp-xxUEy5tG8GU-2d_A2wMvoC2Csoif3q7r1PPZgLeMN-xpVLmNy4AftjzYD-_Rik-FOSzmZ7wReaQP8fRf_L__U-R4pWl5DmRRhig3vCll2_HLWrJ3te_9LYSzfK3N_ws9Em4ftPMCof1YOm_CVwS4TDrC0HdcldgUFGbaMTaDhtqjhWPOuOuOB65A-_PPYSHsqpFxXxtFebg_4K0qYB6Z_GdB7FfPn0xMsL3Ls58m11GLxZUumD4kjKgchkkkIKI9qkr8VQEugB3b_5UnpDA1ZRyqSP4pAHLbJxaFvw9yp_8VeInkS64ALcnE0yWfCWc0ERKsIJhpf7XvEx4mk1oaeKCCCB20Lch1ZCmjXsuPtLXcSFgTStKV4NjlYevENYcRC5Ar_iukrB4PhnqVopEgUe_hreZHnhj5LO16iqBLGu1_Prr9FcI3C6iG5vmSXPSrRKx2jWbH1B7K7EAQH9m-nf6H7BzlhH-0jW-8FbuLXtothwRxYzHMM9i0d86W3TV4TPR6q5wRqwAwwITpfjxYcfU3SRaLhLpUkrzRlR9DwLMqdxKiyJmIDQib_W6WuyVki4E-u3WpFiQg8qxej5OR57aga5_XWDy1YFvELFdFwCyyZoq3HYZmxuHm8w2Cb5uGrvePe3G985n4uKnsYyK9kznRKvQjVh9nNaaLKIFrrRGROZGcCIPqOgKTzhptbswxQH7jBvIKhndNekAEKzbCOe512HLmVgDSkioGycATkqVuRbPFYb8fe2V3403nwe7jSEpF-U24OmoLRYBqH6khZgJgVNjt-LQqb2rdP4W-BqyEbTGbHMdDrRWi0g3yRxwRHqpF2bLKhVsxe_R7Y4JCQZrA3xbWVy3klNX_UVDu5HOVb_K4GUJ_NHOxWhz9lWcaQxQJiian4I6ctNYKxCe6TQdqRw2dXC0HbSRkZg4w9fOsDbA8Zr2rOPxsATsvoBhUYEI549rhqIGZju2_glDiTmEx-UNKOHFVjv0amR_HMDjWF5H8sNaMc1WVDybLH0DJ07_oLJxmnJqb7bv0Sb-CDAAzcGzP9joi2iXZUiKoW_sscKzQODTxBqaid12gGON71U_CUsPq2CV7VRS69IqxcoZy-WjJYd6wwwRTQhe3KuY1_LHGCF2s9cqRbB7tN--D3iC0pSMeKKKvK6gmIp1rSOS2gpwiEshiCb3V5GCF8bK8_ULpOAw-DKhrgxFLOYgfjHLty1pJXHn-SpemEAdERCb5LrV5P3JEBBb1YRD9-0avgXGCFw6pYcFwgcAOTntbyj3PWzpgsYNC14cYKan0nvpmMBXnj-Vtf5GgyK-Utyzb3ekJNHqAgFUTSG_gks7PIogVrr0-nC_6wkAMPXqKTUbDMMe6dUAa0diWBQnzsSbx0",
    "captcha_input_value": "XU3Q",
    "otp_send": "SMS"
}

session.headers.update(headers)

try:
    print(f"\nSending OTP to {otp_url}...")
    
    response_post = session.post(otp_url, json=payload)
    
    print("\n--- API Response ---")
    print(response_post.text)
    
    try:
        print("\n--- Formatted JSON ---")
        print(json.dumps(response_post.json(), indent=2))
    except requests.exceptions.JSONDecodeError:
        print("Response is not in JSON format.")

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the POST request: {e}")