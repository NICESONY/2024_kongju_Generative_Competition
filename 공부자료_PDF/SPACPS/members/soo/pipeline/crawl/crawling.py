'''
아래 url로 접속하시면 자세한 사용법을 볼 수 있습니다.
https://pypi.org/project/bing-image-downloader/
'''

from bing_image_downloader.downloader import download
import glob
import os 
import random

def extract_locations(script):



    locations = []
    tmis=[]


    start_keyword = '추천 장소: '
    start_keyword2 = '특징: '
    lines = script.split('\n')
    print(script)
    

    for line in lines:


        if start_keyword in line:
            
            start_index = line.index(start_keyword)+2 + len(start_keyword)
            location = line[start_index:].strip()
            locations.append(location)

        elif start_keyword2 in line:
            start_index = line.index(start_keyword2)+2 + len(start_keyword2)
            tmi = line[start_index:].strip()
            tmis.append(tmi)
        else:
            pass

            #tmis.append()
            
    
    return locations,tmis


   

def retrieve(query_string,user):    
    
    download(query_string, limit=5,  output_dir=f'{user}/dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True, filter='jpg')
    
    list=glob.glob(f"{user}/dataset/{query_string}/*.png")
    list+=glob.glob(f"{user}/dataset/{query_string}/*.jpg")
    list+=glob.glob(f"{user}/dataset/{query_string}/*.jpeg")
    list=sorted(list)
    #random.shuffle(list)
    

    return list[0]
