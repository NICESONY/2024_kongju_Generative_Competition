import requests
from bs4 import BeautifulSoup
import os

def get_google_image_urls(query, num_images=5):
    #query = query.replace(' ', '+')
    url = f"https://www.google.com/search?hl=en&tbm=isch&q={query}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_elements = soup.find_all('img', limit=num_images + 1)
    
    image_urls = []
    for img in image_elements[1:num_images + 1]:  # 첫 번째 이미지는 구글 로고일 가능성이 높음
        print(img)
        try:
            image_urls.append(img['src'])
        except KeyError:
            continue
    #print(image_urls)
    return image_urls

def download_images(image_urls, folder_path='images'):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    for i, url in enumerate(image_urls):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(os.path.join(folder_path, f'image_{i+1}.jpg'), 'wb') as file:
                    file.write(response.content)
                print(f"Downloaded image {i+1}")
            else:
                print(f"Failed to download image {i+1}: Status code {response.status_code}")
        except Exception as e:
            print(f"Error downloading image {i+1}: {e}")

query = "puppies"
image_urls = get_google_image_urls(query)
download_images(image_urls)
