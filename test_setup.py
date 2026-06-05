import requests
from dotenv import load_dotenv
import os

# Test 1 — requests works
response = requests.get("https://httpbin.org/get")
print("✅ requests works! Status code:", response.status_code)

# Test 2 — dotenv works
with open(".env", "w") as f:
    f.write("TEST_KEY=hello_from_env\n")

load_dotenv()
value = os.getenv("TEST_KEY")
print("✅ dotenv works! Value:", value)