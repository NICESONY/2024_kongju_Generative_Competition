import torch
from transformers import BlipForImageTextRetrieval

model = BlipForImageTextRetrieval.from_pretrained("Salesforce/blip-itm-base-coco")
print(model)