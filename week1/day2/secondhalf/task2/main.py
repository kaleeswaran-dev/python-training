import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")


def safe_get(url, timeout=5, retries=3, **kwargs):

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=timeout, **kwargs)
            response.raise_for_status()
            return response

        except requests.exceptions.Timeout:
            print(f"Attempt {attempt}: Request timed out")

            if attempt == retries:
                print("Maximum retries reached")
                return None

        except requests.exceptions.ConnectionError:
            print("Connection error occurred")
            return None

        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
            return None



try:
    headers = {
        "X-API-Key": API_KEY
    }

    response = requests.get(
        "https://httpbin.org/headers",
        headers=headers,
        timeout=5
    )

    response.raise_for_status()

    data = response.json()

    print(
        "Server received key:",
        data.get("headers", {}).get("X-Api-Key")
    )

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Connection error")

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)



try:
    requests.get(
        "https://httpbin.org/delay/10",
        timeout=3
    )

except requests.exceptions.Timeout:
    print("Timeout after 3 seconds: please try again")



try:
    response = requests.get(
        "https://httpbin.org/status/500",
        timeout=5
    )

    response.raise_for_status()

except requests.exceptions.HTTPError:
    print("Server error 500 handled")



try:
    response = requests.get(
        "https://httpbin.org/json",
        timeout=5
    )

    response.raise_for_status()

    data = response.json()

    result = {
        "title": data.get("slideshow", {}).get("title"),
        "author": data.get("slideshow", {}).get("author")
    }

    with open("result.json", "w") as file:
        json.dump(result, file, indent=4)

    print("Result saved to result.json")

except Exception as e:
    print("Error:", e)



print("\nTesting safe_get()")

safe_get(
    "https://httpbin.org/delay/10",
    timeout=3
)