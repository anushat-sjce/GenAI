import requests
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

#load the pretrained processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

#load the image, Dont forget to write your image name
img_path = "cheetah.jpg"

#convert it into an RGB format
image = Image.open(img_path).convert('RGB')

#You do not need a question for image captioning
text = "the image of"
inputs = processor(images=image, text=text, return_tensors="pt")

#Generate a caption for the image
outputs = model.generate(**inputs, max_length=50)

#Decode the generated tokens to text
caption = processor.decode(outputs[0], skip_special_tokens=True)

#print the caption
print(caption)
