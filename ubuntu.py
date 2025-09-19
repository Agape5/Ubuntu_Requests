import os
import requests
from urllib.parse import urlparse
from uuid import uuid4

def get_filename_from_url(url):
    parsed = urlparse(url)
    filename = os.path.basename(parsed.path)
    if not filename or '.' not in filename:
        filename = f"image_{uuid4().hex}.jpg"
    return filename

def fetch_and_save_image(url, directory="Fetched_Images"):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        filename = get_filename_from_url(url)
        filepath = os.path.join(directory, filename)

        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✅ Image saved to: {filepath}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching image: {e}")

def main():
    print("🌍 Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    url = input("Please enter the image URL: ").strip()

    os.makedirs("Fetched_Images", exist_ok=True)
    fetch_and_save_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()