import json
import base64
import requests

def ocr_clova(path2):

    with open(path2, "rb") as f:
        img = base64.b64encode(f.read())

    URL = "url"
    KEY = "key"
        
    headers = {
        "Content-Type": "application/json",
        "X-OCR-SECRET": KEY
    }
    #"/root/naver/members/soo/pipeline/user_input/gradio_input.png"
    data = {
        "version": "V1",
        "requestId": "sample_id", 
        "timestamp": 0,
        "images": [
            {
                "name": path2.split(".")[0],  #/root/naver/members/soo/pipeline/user_input/
                "format": path2.split(".")[1],
                "data": img.decode('utf-8')
            }
        ]
    }
    data = json.dumps(data)
    response = requests.post(URL, data=data, headers=headers)
    res = json.loads(response.text)
    out_list=res["fields"]
    main_list=[]
    for i in range(len(out_list)):
        main_list.append(out_list[i]["inferText"])
    

    return str(main_list)



