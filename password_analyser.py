import requests
import hashlib

pwd = input("Enter the password to check: ")
hashed = hashlib.sha1(pwd.encode('utf-8')).hexdigest().upper()
prefix = hashed[:5]
suffix = hashed[5:]

url = "https://api.pwnedpasswords.com/range/"

response = requests.get(f"{url}{prefix}")

if suffix in response.text:
    print("Password has been compromised!")
else:
    print("Password is safe.")
    