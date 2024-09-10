from selenium import webdriver 
from bs4 import BeautifulSoup as soups

def search_selenium(search_name, search_path, search_limit) :
    search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"

    #from selenium import webdriver

    cService = webdriver.ChromeService(executable_path='/usr/bin/chromedriver')
    #driver = webdriver.Chrome(service = cService)
    
    browser = webdriver.Chrome(service=cService)
    browser.get(search_url)
    
    image_count = len(browser.find_elements_by_tag_name("img"))
    
    print("로드된 이미지 개수 : ", image_count)

    browser.implicitly_wait(2)

    for i in range( search_limit ) :
        image = browser.find_elements_by_tag_name("img")[i]
        image.screenshot("/home/ssac15/aiffel/face_embedding/images/" + str(i) + ".png")

    browser.close()

if __name__ == "__main__" :

    search_name = "dog"
    search_limit = int(2)
    search_path = "/root/naver/members/soo/search/imgs"
    # search_maybe(search_name, search_limit, search_path)
    search_selenium(search_name, search_path, search_limit)
