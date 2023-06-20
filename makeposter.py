import json
import requests
import io
import base64
import openai
import argparse
from PIL import Image, PngImagePlugin

sd_url = "http://127.0.0.1:7860"

argParser = argparse.ArgumentParser()
argParser.add_argument('-p', '--prompt', help = 'the main word for the poster', default = 'Prompt')
argParser.add_argument('-d', '--demotivate', help = 'makes a demotivational instead of a motivational', action = 'store_true')

args = argParser.parse_args()


demotivate = args.demotivate
prompt = args.prompt

apifile = open('apikey.txt')
openai.api_key = apifile.read()

def generateimage(apitype,payload):
    response = requests.post(url=f'{sd_url}/sdapi/v1/' + apitype, json=payload)
    r = response.json()
    if 'images' in r:
        print('found images!')
    else:
        print('ERROR!')
        print(r)
    return r['images'][0]

def saveb64(imgb64, filename):
    image = Image.open(io.BytesIO(base64.b64decode(imgb64.split(",",1)[0])))
    image.save(filename)
    

def loadb64(filename):
    img = Image.open(filename)
    imgfile = io.BytesIO()
    img.save(imgfile, format='PNG')
    imgb64 = base64.b64encode(imgfile.getvalue()).decode("utf-8") 
    #imgb64 = imgb64[2:-1]
    return imgb64
    
def chatgpt(m):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = m
    )
    return response.choices[0].message.content



"""

print(chatgpt([
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What was the name of the first cat in space?"}
]))

payload1 = {
    "prompt": prompt,
    "steps": 20,
    "width": 1024,
    "height": 512,
    "override_settings": {
        "sd_model_checkpoint": "v1-5-pruned-emaonly.safetensors [6ce0161689]"
    }
}
step1b64 = generateimage('txt2img', payload1)

saveb64(step1b64,'step1.png')

mask = loadb64('1024mask.png')

payload2 = {
    "init_images": [
        "data:image/png;base64," + step1b64
    ],
    "mask": "data:image/png;base64," + mask,
    "prompt": prompt,
    "steps": 20,
    "width": 1024,
    "height": 512,
    "tiling": True,
    "denoising_strength": 0.75,
    "image_cfg_scale": 0,
    "mask_blur": 4,
    "inpainting_fill": 1, #THE ANNOYING ONE THAT BROKE EVERYTHING (most of the rest of this can probably be removed?)
    "inpaint_full_res": True,
    "inpaint_full_res_padding": 0,
    "inpainting_mask_invert": 0,
    "initial_noise_multiplier": 0,  "seed": -1,
    "subseed": -1,
    "subseed_strength": 0,
    "seed_resize_from_h": -1,
    "seed_resize_from_w": -1,
    "sampler_name": "Euler a",
    "batch_size": 1,
    "n_iter": 1,
    "cfg_scale": 7,
    "sampler_index": "Euler a",
    "override_settings": {
        "sd_model_checkpoint": "v1-5-pruned-emaonly.safetensors [6ce0161689]"
    }
    
    
    
}
step2b64 = generateimage('img2img',payload2)

saveb64(step2b64,'step2.png')
"""
