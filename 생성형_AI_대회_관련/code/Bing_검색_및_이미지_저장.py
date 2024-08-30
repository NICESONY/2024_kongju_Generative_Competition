# Bing 검색  및  이미지 다운로드

import requests
import os
import cv2
import numpy as np

# Bing Search API 키와 엔드포인트 설정
api_key = 'YOUR_BING_API_KEY'
endpoint = 'https://api.bing.microsoft.com/v7.0/images/search'
headers = {'Ocp-Apim-Subscription-Key': api_key}

def search_images(query):
    params = {'q': query, 'license': 'public', 'imageType': 'photo'}
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    return search_results['value']

def download_image(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

# 이미지 검색 및 다운로드
query = 'beautiful landscapes'
images = search_images(query)
for i, image in enumerate(images[:5]):  # 첫 5개 이미지 다운로드
    download_image(image['contentUrl'], f'image_{i}.jpg')
